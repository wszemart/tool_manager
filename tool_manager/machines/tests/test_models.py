from django.test import TestCase
from django.urls import reverse
from users.factories import UserFactory
from machines.factories import MachineFactory


class MachineModelTestCase(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.machine = MachineFactory(author=self.user)

    def test_machine_absolute_url(self):
        url = reverse('machine-detail', kwargs={'pk': self.machine.pk})
        self.assertEqual(self.machine.get_absolute_url(), url)
