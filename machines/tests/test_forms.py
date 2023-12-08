from django.test import TestCase

from machines.factories import MachineFactory
from machines.forms import MachineForm


class MachineFormTestCase(TestCase):
    def test_valid_machine_form(self):
        form = MachineForm(
            data={
                "name": "Test Machine",
                "description": "Test description",
            }
        )
        self.assertTrue(form.is_valid())

    def test_blank_machine_form(self):
        form = MachineForm(data={})
        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 2)

    def test_machine_form_with_missing_name(self):
        form = MachineForm(
            data={
                "description": "Test description",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("name", form.errors)

    def test_machine_form_with_missing_description(self):
        form = MachineForm(
            data={
                "name": "Test Machine",
            }
        )
        self.assertFalse(form.is_valid())
        self.assertIn("description", form.errors)

    def test_machine_form_with_factory(self):
        machine = MachineFactory()
        form = MachineForm(
            data={
                "name": machine.name,
                "description": machine.description,
            }
        )
        self.assertTrue(form.is_valid())
