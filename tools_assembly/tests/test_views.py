from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from django.test import Client, TestCase
from django.urls import reverse

from holders.factories import HolderFactory
from machines.factories import MachineFactory
from tools.factories import ToolFactory
from tools.models import Tool
from tools_assembly.factories import ToolAssemblyFactory
from users.factories import UserFactory

from ..models import ToolAssembly


class TestToolAssemblyViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.user_with_permission = UserFactory()
        self.user_without_permission = UserFactory()

        content_type = ContentType.objects.get_for_model(ToolAssembly)

        permission_add_toolassembly = Permission.objects.get(content_type=content_type, codename="add_toolassembly")
        permission_change_toolassembly = Permission.objects.get(
            content_type=content_type, codename="change_toolassembly"
        )
        permission_delete_toolassembly = Permission.objects.get(
            content_type=content_type, codename="delete_toolassembly"
        )
        self.user_with_permission.user_permissions.add(
            permission_add_toolassembly,
            permission_change_toolassembly,
            permission_delete_toolassembly,
        )
        self.tool = ToolFactory()
        self.toolassembly = ToolAssemblyFactory(author=self.user_with_permission, tool=self.tool)
        self.machine = MachineFactory()
        self.holder = HolderFactory()
        self.toolassembly_detail_url = reverse("tool-assembly-detail", kwargs={"pk": self.toolassembly.pk})
        self.toolassembly_create_url = reverse("tool-assembly-create")
        self.toolassembly_update_url = reverse("tool-assembly-update", kwargs={"pk": self.toolassembly.pk})
        self.toolassembly_delete_url = reverse("tool-assembly-delete", kwargs={"pk": self.toolassembly.pk})
        self.data = {
            "tool_nr": 1,
            "radius": 8.0,
            "total_length": 300.0,
            "outside_holder": 150.0,
            "machine": self.machine.pk,
            "holder": self.holder.pk,
            "tool": self.tool.pk,
        }

    def test_toolassembly_detail_view(self):
        response = self.client.get(self.toolassembly_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tools_assembly/tool_assembly_detail.html")

    def test_toolassembly_create_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.post(self.toolassembly_create_url, data=self.data)
        self.assertRedirects(response, reverse("tool-assembly"), status_code=302)
        self.assertEqual(ToolAssembly.objects.count(), 2)

    def test_toolassembly_create_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.post(self.toolassembly_create_url, data=self.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Tool.objects.count(), 1)

    def test_toolassembly_update_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.toolassembly_update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "tools_assembly/tool_assembly_form.html")

    def test_toolassembly_update_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.toolassembly_update_url)
        self.assertEqual(response.status_code, 403)

    def test_toolassembly_delete_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        self.assertEqual(ToolAssembly.objects.count(), 1)
        response = self.client.post(self.toolassembly_delete_url)
        self.assertEqual(ToolAssembly.objects.count(), 0)
        self.assertEqual(response.status_code, 302)

    def test_toolassembly_delete_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.post(self.toolassembly_delete_url)
        self.assertEqual(ToolAssembly.objects.count(), 1)
        self.assertEqual(response.status_code, 403)
