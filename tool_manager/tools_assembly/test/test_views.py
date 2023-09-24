from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Permission
from django.contrib.contenttypes.models import ContentType
from ..models import Holder


class TestHolderViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
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
        self.user.user_permissions.add(
            permission_add_holder,
            permission_change_holder,
            permission_delete_holder,
        )
        self.client.login(username='testuser', password='testpassword')
        self.holder = Holder.objects.create(
            holder_type= 'type_1',
            catalog_nr= 'Katalog123',
            inner_diameter=5.0,
            LH1=1.0,
            DH1_A=2.0,
            author=self.user
        )
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
            'author': self.user
        }

    def test_holder_detail_view(self):
        response = self.client.get(self.holder_detail_url)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'tools_assembly/holder_detail.html')
