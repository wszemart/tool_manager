from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from ..models import Holder, Tool, ToolAssembly, UserComment
from users.factories import UserFactory
from tools_assembly.factories import HolderFactory, ToolFactory, ToolAssemblyFactory
from machines.factories import MachineFactory


class TestHolderViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_with_permission = UserFactory()
        self.user_without_permission = UserFactory()

        content_type = ContentType.objects.get_for_model(Holder)

        permission_add_holder = Permission.objects.get(
            content_type=content_type,
            codename='add_holder'
        )
        permission_change_holder = Permission.objects.get(
            content_type=content_type,
            codename='change_holder'
        )
        permission_delete_holder = Permission.objects.get(
            content_type=content_type,
            codename='delete_holder'
        )
        self.user_with_permission.user_permissions.add(
            permission_add_holder,
            permission_change_holder,
            permission_delete_holder,
        )

        self.holder = HolderFactory(author=self.user_with_permission)
        self.holder_detail_url = reverse('holder-detail', kwargs={'pk': self.holder.pk})
        self.holder_create_url = reverse('holder-create')
        self.holder_update_url = reverse('holder-update', kwargs={'pk': self.holder.pk})
        self.holder_delete_url = reverse('holder-delete', kwargs={'pk': self.holder.pk})
        self.data = {
            'holder_type': 'type_1',
            'catalog_nr': 'Katalog123',
            'inner_diameter': 5.0,
            'LH1': 1.0,
            'DH1_A': 2.0,
            'author': self.user_with_permission
        }

    def test_holder_detail_view(self):
        response = self.client.get(self.holder_detail_url)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools_assembly/holder_detail.html')

    def test_holder_create_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.post(self.holder_create_url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Holder.objects.count(), 2)
        holder = Holder.objects.last()
        self.assertEqual(holder.catalog_nr, 'Katalog123')

    def test_holder_create_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.post(self.holder_create_url, data=self.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Holder.objects.count(), 1)

    def test_holder_update_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.holder_update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools_assembly/holder_form.html')

    def test_holder_update_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.holder_update_url)
        self.assertEqual(response.status_code, 403)

    def test_holder_delete_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        self.assertEqual(Holder.objects.count(), 1)
        response = self.client.post(self.holder_delete_url)
        self.assertEqual(Holder.objects.count(), 0)
        self.assertEqual(response.status_code, 302)

    def test_holder_delete_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.post(self.holder_delete_url)
        self.assertEqual(Holder.objects.count(), 1)
        self.assertEqual(response.status_code, 403)


class TestToolViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_with_permission = UserFactory()
        self.user_without_permission = UserFactory()

        content_type = ContentType.objects.get_for_model(Tool)

        permission_add_tool = Permission.objects.get(
            content_type=content_type,
            codename='add_tool'
        )
        permission_change_tool = Permission.objects.get(
            content_type=content_type,
            codename='change_tool'
        )
        permission_delete_tool = Permission.objects.get(
            content_type=content_type,
            codename='delete_tool'
        )
        self.user_with_permission.user_permissions.add(
            permission_add_tool,
            permission_change_tool,
            permission_delete_tool,
        )

        self.tool = ToolFactory(author=self.user_with_permission)
        self.tool_detail_url = reverse('tool-detail', kwargs={'pk': self.tool.pk})
        self.tool_create_url = reverse('tool-create')
        self.tool_update_url = reverse('tool-update', kwargs={'pk': self.tool.pk})
        self.tool_delete_url = reverse('tool-delete', kwargs={'pk': self.tool.pk})
        self.data = {
            'tool_type': 'type_1',
            'catalog_nr': 'Katalog123',
            'R': 5.0,
            'L1': 1.0,
            'D1': 2.0,
            'L2': 1.0,
            'D2': 2.0,
            'L3': 1.0,
            'D3': 2.0,
            'L4': 1.0,
            'D4': 2.0,
            'author': self.user_with_permission
        }

    def test_tool_detail_view(self):
        response = self.client.get(self.tool_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools_assembly/tool_detail.html')

    def test_tool_create_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.post(self.tool_create_url, data=self.data)
        # self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tool'), status_code=302)
        self.assertEqual(Tool.objects.count(), 2)
        tool = Tool.objects.last()
        self.assertEqual(tool.catalog_nr, 'Katalog123')

    def test_tool_create_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.post(self.tool_create_url, data=self.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Tool.objects.count(), 1)

    def test_tool_update_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.tool_update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools_assembly/tool_form.html')

    def test_tool_update_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.get(self.tool_update_url)
        self.assertEqual(response.status_code, 403)

    def test_tool_delete_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        self.assertEqual(Tool.objects.count(), 1)
        response = self.client.post(self.tool_delete_url)
        self.assertEqual(Tool.objects.count(), 0)
        self.assertEqual(response.status_code, 302)

    def test_tool_delete_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.post(self.tool_delete_url)
        self.assertEqual(Tool.objects.count(), 1)
        self.assertEqual(response.status_code, 403)


class TestToolAssemblyViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user_with_permission = UserFactory()
        self.user_without_permission = UserFactory()

        content_type = ContentType.objects.get_for_model(Tool)

        permission_add_toolassembly = Permission.objects.get(
            content_type=content_type,
            codename='add_toolassembly'
        )
        permission_change_toolassembly = Permission.objects.get(
            content_type=content_type,
            codename='change_toolassembly'
        )
        permission_delete_toolassembly = Permission.objects.get(
            content_type=content_type,
            codename='delete_toolassembly'
        )
        self.user_with_permission.user_permissions.add(
            permission_add_toolassembly,
            permission_change_toolassembly,
            permission_delete_toolassembly,
        )

        self.toolassembly = ToolAssemblyFactory(author=self.user_with_permission)
        self.machine = MachineFactory()
        self.holder = HolderFactory()
        self.tool = ToolFactory()
        self.toolassembly_detail_url = reverse('tool-assembly-detail', kwargs={'pk': self.toolassembly.pk})
        self.toolassembly_create_url = reverse('tool-assembly-create')
        self.toolassembly_update_url = reverse('tool-assembly-update', kwargs={'pk': self.toolassembly.pk})
        self.toolassembly_delete_url = reverse('tool-assembly-delete', kwargs={'pk': self.toolassembly.pk})
        self.data = {
            'tool_nr': 1,
            'radius': 8.0,
            'total_length': 300.0,
            'outside_holder': 150.0,
            'machine': self.machine.pk,
            'holder': self.holder.pk,
            'tool': self.tool.pk,
        }

    def test_toolassembly_detail_view(self):
        response = self.client.get(self.toolassembly_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools_assembly/tool_assembly_detail.html')

    def test_toolassembly_create_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.post(self.toolassembly_create_url, data=self.data)
        # self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('tool_assembly'), status_code=302)
        self.assertEqual(ToolAssembly.objects.count(), 2)
        tool = ToolAssembly.objects.last()
        self.assertEqual(tool.catalog_nr, 'Katalog123')

    def test_toolassembly_create_view_without_permission(self):
        self.client.force_login(self.user_without_permission)
        response = self.client.post(self.toolassembly_create_url, data=self.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Tool.objects.count(), 1)

    def test_toolassembly_update_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.get(self.toolassembly_update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools_assembly/tool_assembly_form.html')

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
