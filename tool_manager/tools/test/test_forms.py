from django.test import TestCase
from ..forms import ToolForm
from users.factories import UserFactory


class ToolFormTest(TestCase):

    def setUp(self) -> None:

        self.user = UserFactory()
        self.valid_data = {
            'tool_type': 'end_mill',
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
            'author': self.user
        }

        self.invalid_data = {
            'tool_type': 'test_type',
            'catalog_nr': 124,
            'R': 'This is not a number',
            'L1': 'This is not a number',
            'D1': 'This is not a number',
            'L2': 'This is not a number',
            'D2': 'This is not a number',
            'L3': 'This is not a number',
            'D3': 'This is not a number',
            'L4': 'This is not a number',
            'D4': 'This is not a number',
            'author': 'user'
        }

    def test_valid_form(self):
        form = ToolForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = ToolForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
