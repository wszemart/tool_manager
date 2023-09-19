from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from machines.models import Machine


class MachineModelTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.machine = Machine.objects.create(
            name='Test Machine',
            description='Test description',
            author=self.user
        )

    def test_machine_absolute_url(self):
        url = reverse('machine-detail', kwargs={'pk': self.machine.pk})
        self.assertEqual(self.machine.get_absolute_url(), url)
