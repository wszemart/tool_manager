from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType
from ..models import Holder
from users.factories import UserFactory
from holders.factories import HolderFactory


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
        self.assertTemplateUsed(response, 'holders/holder_detail.html')

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
        self.assertTemplateUsed(response, 'holders/holder_form.html')

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
