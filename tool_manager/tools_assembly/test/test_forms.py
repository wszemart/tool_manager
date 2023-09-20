from django.test import TestCase
from django.contrib.auth.models import User
from ..forms import HolderForm, ToolForm, ToolAssemblyForm, ToolAssemblySlim
from ..models import Holder, Tool
from machines.models import Machine


class HolderFormTest(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
        self.valid_data = {
            'holder_type': 'type_1',
            'catalog_nr': 'Katalog123',
            'inner_diameter': 5.0,
            'LH1': 1.0,
            'DH1_A': 2.0,
            'author': self.user
        }

        self.invalid_data = {
            'holder_type': 'test_type',
            'catalog_nr': 'This is not a number',
            'inner_diameter': 'This is not a number',
            'LH1': 'This is not a number',
            'DH1_A': 'This is not a number',
            'author': 'user'
        }

    def test_valid_form(self):
        form = HolderForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form = HolderForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())


class ToolFormTest(TestCase):

    def setUp(self) -> None:

        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )
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
        form = HolderForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())


class ToolAssemblyFormTest(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        self.machine = Machine.objects.create(
            name='Test Machine',
            description='Test description'
        )
        self.holder = Holder.objects.create(
            holder_type='type_1',
            inner_diameter=12,
            catalog_nr='Catalog123',
            author=self.user

        )
        self.tool = Tool.objects.create(
            tool_type='end_mill',
            catalog_nr='Catalog123',
            author=self.user,
        )
        self.valid_data = {
            'tool_nr': 1,
            'radius': 12.5,
            'total_length': 250.0,
            'outside_holder': 100.0,
            'machine': self.machine,
            'holder': self.holder,
            'tool': self.tool,
            'author': self.user
        }

        self.invalid_data = {
            'tool_nr': 'This is not a number',
            'radius': 'This is not a number',
            'total_length': -50.0,
            'outside_holder': 'This is not a number',
            'machine': 'Machine',
            'holder': 'Holder',
            'tool': 'Tool',
            'author': 'user'
        }

        self.form = ToolAssemblySlim(data=self.valid_data)

    def test_toolassembly_valid_form(self):
        form = ToolAssemblyForm(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_tool_assembly_invalid_form(self):
        form = ToolAssemblyForm(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_toolassemblyslim_valid_form(self):
        form = ToolAssemblySlim(data=self.valid_data)
        self.assertTrue(form.is_valid())

    def test_toolassemblyslim_invalid_form(self):
        form = ToolAssemblySlim(data=self.invalid_data)
        self.assertFalse(form.is_valid())

    def test_form_fields_disabled(self):
        self.assertEqual(self.form.fields['tool_nr'].widget.attrs.get('disabled'), 'disabled')
        self.assertEqual(self.form.fields['machine'].widget.attrs.get('disabled'), 'disabled')
        self.assertEqual(self.form.fields['holder'].widget.attrs.get('disabled'), 'disabled')
        self.assertEqual(self.form.fields['tool'].widget.attrs.get('disabled'), 'disabled')
