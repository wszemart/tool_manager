from django.test import TestCase, Client, tag
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from ..models import Tool
from users.factories import UserFactory
from tools.factories import ToolFactory


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
            'tool_type': 'drill',
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
        self.assertTemplateUsed(response, 'tools/tool_detail.html')

    def test_tool_create_view_with_permission(self):
        self.client.force_login(self.user_with_permission)
        response = self.client.post(self.tool_create_url, data=self.data)
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
        self.assertTemplateUsed(response, 'tools/tool_form.html')

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
