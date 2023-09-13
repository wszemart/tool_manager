from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import home, MachineListView, MachineDetailView, MachineCreateView, MachineUpdateView, MachineDeleteView


class TestUrls(SimpleTestCase):

    def test_app_home_is_resolved(self):
        url = reverse('app-home')
        print(resolve(url))
        self.assertEqual(resolve(url).func, home)

