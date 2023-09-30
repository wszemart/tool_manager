from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import HolderListView, HolderUpdateView, HolderDetailView, HolderCreateView, HolderDeleteView


class TestUrls(SimpleTestCase):

    def test_holder_list_is_resolved(self):
        url = reverse('holder')
        self.assertEqual(resolve(url).func.view_class, HolderListView)
        self.assertEqual(resolve(url).url_name, 'holder')

    def test_holder_create_is_resolved(self):
        url = reverse('holder-create')
        self.assertEqual(resolve(url).func.view_class, HolderCreateView)
        self.assertEqual(resolve(url).url_name, 'holder-create')

    def test_holder_update_is_resolved(self):
        url = reverse('holder-update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, HolderUpdateView)
        self.assertEqual(resolve(url).url_name, 'holder-update')

    def test_holder_detail_is_resolved(self):
        url = reverse('holder-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, HolderDetailView)
        self.assertEqual(resolve(url).url_name, 'holder-detail')

    def test_holder_delete_is_resolved(self):
        url = reverse('holder-delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, HolderDeleteView)
        self.assertEqual(resolve(url).url_name, 'holder-delete')
