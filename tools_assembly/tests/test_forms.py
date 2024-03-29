from django.test import TestCase, tag

from holders.factories import HolderFactory
from machines.factories import MachineFactory
from tools.factories import ToolFactory
from users.factories import UserFactory

from ..forms import ToolAssemblyForm, ToolAssemblySlim


class ToolAssemblyFormTest(TestCase):
    def setUp(self) -> None:
        self.user = UserFactory()
        self.machine = MachineFactory()
        self.holder = HolderFactory()
        self.tool = ToolFactory()
        self.valid_data = {
            "tool_nr": 1,
            "radius": 12.5,
            "total_length": 250.0,
            "outside_holder": 100.0,
            "machine": self.machine,
            "holder": self.holder,
            "tool": self.tool,
            "author": self.user,
        }

        self.invalid_data = {
            "tool_nr": "This is not a number",
            "radius": "This is not a number",
            "total_length": -50.0,
            "outside_holder": "This is not a number",
            "machine": "Machine",
            "holder": "Holder",
            "tool": "Tool",
            "author": "user",
        }

        self.valid_slim_data = {
            "radius": 12.5,
            "total_length": 250.0,
            "outside_holder": 100.0,
            "author": self.user,
        }

    def test_tool_assembly_valid_form(self):
        form = ToolAssemblyForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_tool_assembly_invalid_form(self):
        form = ToolAssemblyForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    @tag("x")
    def test_tool_assembly_slim_valid_form(self):
        form = ToolAssemblySlim(data=self.valid_slim_data)
        self.assertTrue(form.is_valid())

    def test_tool_assembly_slim_invalid_form(self):
        form = ToolAssemblySlim(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_form_fields_disabled(self):
        form = ToolAssemblySlim(data=self.valid_data)
        self.assertEqual(form.fields["tool_nr"].disabled, True)
        self.assertEqual(form.fields["machine"].disabled, True)
        self.assertEqual(form.fields["holder"].disabled, True)
        self.assertEqual(form.fields["tool"].disabled, True)
