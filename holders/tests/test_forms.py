from django.test import TestCase

from users.factories import UserFactory

from ..forms import HolderForm


class HolderFormTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.valid_data = {
            "holder_type": "type_1",
            "catalog_nr": "Katalog123",
            "inner_diameter": 5.0,
            "LH1": 1.0,
            "DH1_A": 2.0,
            "author": self.user,
        }

        self.invalid_data = {
            "holder_type": "test_type",
            "catalog_nr": "This is not a number",
            "inner_diameter": "This is not a number",
            "LH1": "This is not a number",
            "DH1_A": "This is not a number",
            "author": "user",
        }

    def test_valid_form(self):
        form = HolderForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = HolderForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())
