from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import home, MachineDetailView, MachineCreateView, MachineUpdateView, MachineDeleteView, generate_csv, generic_pdf


class TestUrls(SimpleTestCase):

    def test_app_home_is_resolved(self):
        url = reverse('app-home')
        self.assertEqual(resolve(url).func, home)

    def test_machine_detail_is_resolved(self):
        url = reverse('machine-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, MachineDetailView)
        self.assertEqual(resolve(url).url_name, 'machine-detail')

    def test_machine_create_is_resolved(self):
        url = reverse('machine-create')
        self.assertEqual(resolve(url).func.view_class, MachineCreateView)
        self.assertEqual(resolve(url).url_name, 'machine-create')

    def test_machine_update_is_resolved(self):
        url = reverse('machine-update', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, MachineUpdateView)
        self.assertEqual(resolve(url).url_name, 'machine-update')

    def test_machine_delete_is_resolved(self):
        url = reverse('machine-delete', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, MachineDeleteView)
        self.assertEqual(resolve(url).url_name, 'machine-delete')

    def test_generate_csv_is_resolved(self):
        url = reverse('generate-csv')
        self.assertEqual(resolve(url).func, generate_csv)
        self.assertEqual(resolve(url).url_name, 'generate-csv')

    def test_generate_pdf_is_resolved(self):
        url = reverse('generate-pdf')
        self.assertEqual(resolve(url).func, generic_pdf)
        self.assertEqual(resolve(url).url_name, 'generate-pdf')
