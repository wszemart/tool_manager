from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from machines.models import Machine


class TestMachineViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        content_type = ContentType.objects.get_for_model(Machine)

        permission_add_machine = Permission.objects.get(
            content_type=content_type,
            codename='add_machine'
        )
        permission_change_machine = Permission.objects.get(
            content_type=content_type,
            codename='change_machine'
        )
        permission_delete_machine = Permission.objects.get(
            content_type=content_type,
            codename='delete_machine'
        )
        self.user.user_permissions.add(
            permission_add_machine,
            permission_change_machine,
            permission_delete_machine,
        )
        self.client.login(username='testuser', password='testpassword')
        self.machine = Machine.objects.create(
            name='Test Machine',
            description='Test description'
        )
        self.machine_detail_url = reverse('machine-detail', kwargs={'pk': self.machine.pk})
        self.machine_create_url = reverse('machine-create')
        self.machine_update_url = reverse('machine-update', kwargs={'pk': self.machine.pk})
        self.machine_delete_url = reverse('machine-delete', kwargs={'pk': self.machine.pk})
        self.data = {
            'name': 'Test Machine',
            'description': 'Test description'
        }

    def test_machine_detail_view(self):
        response = self.client.get(self.machine_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'machines/machine_detail.html')
        self.assertContains(response, 'Test Machine')

    def test_machine_create_view_with_permission(self):
        response = self.client.post(self.machine_create_url, data=self.data)
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Machine.objects.count(), 2)
        machine = Machine.objects.last()
        self.assertEqual(machine.name, 'Test Machine')

    def test_machine_create_view_without_permission(self):
        machine_permission = Permission.objects.get(codename='add_machine')
        self.user.user_permissions.remove(machine_permission)
        response = self.client.post(self.machine_create_url, data=self.data)
        self.assertEqual(response.status_code, 403)
        self.assertEqual(Machine.objects.count(), 1)

    def test_machine_update_view_with_permission(self):
        response = self.client.get(self.machine_update_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'machines/machine_form.html')

    def test_machine_update_view_without_permission(self):
        machine_permission = Permission.objects.get(codename='change_machine')
        self.user.user_permissions.remove(machine_permission)
        response = self.client.get(self.machine_update_url)
        self.assertEqual(response.status_code, 403)

    def test_machine_delete_view_with_permission(self):
        response = self.client.post(self.machine_delete_url)
        self.assertEqual(Machine.objects.count(), 0)
        self.assertEqual(response.status_code, 302)
        with self.assertRaises(Machine.DoesNotExist):
            self.machine.refresh_from_db()

    def test_machine_delete_view_without_permission(self):
        machine_permission = Permission.objects.get(codename='delete_machine')
        self.user.user_permissions.remove(machine_permission)
        response = self.client.post(self.machine_delete_url)
        self.assertEqual(Machine.objects.count(), 1)
        self.assertEqual(response.status_code, 403)
