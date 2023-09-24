from django import forms
from django.core.exceptions import ValidationError
from .models import Holder, Tool, ToolAssembly, UserComment
from django.core.validators import MinValueValidator, MaxValueValidator


class HolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = ['holder_type', 'inner_diameter', 'catalog_nr', 'LH1', 'DH1_A', 'DH1_B', 'LH2', 'DH2', 'LH3', 'DH3']
        labels = {
            'holder_type': 'Typ oprawki',
            'catalog_nr': 'Nr katalogowy',
            'inner_diameter': 'Średnica wewnętrzna'
        }

    def clean(self):
        cleaned_data = super().clean()
        fields_to_check = ['inner_diameter', 'LH1', 'DH1_A', 'DH1_B', 'LH2', 'DH2', 'LH3', 'DH3']
        for field_name in fields_to_check:
            field_value = cleaned_data.get(field_name)
            if field_value is not None and field_value <= 0:
                self.add_error(field_name, f"Wartość {field_name} musi być większa niż 0.")

        return cleaned_data


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool_type', 'catalog_nr', 'R', 'L1', 'D1', 'L2', 'D2', 'L3', 'D3', 'L4', 'D4']
        labels = {
            'tool_type': 'Typ freza',
            'catalog_nr': 'Nr katalogowy',
        }

    def clean(self):
        cleaned_data = super().clean()
        fields_to_check = ['R', 'L1', 'D1', 'L2', 'D2', 'L3', 'D3', 'L4', 'D4']
        for field_name in fields_to_check:
            field_value = cleaned_data.get(field_name)
            if field_value is not None and field_value <= 0:
                self.add_error(field_name, f"Wartość {field_name} musi być większa niż 0.")

        return cleaned_data


class ToolAssemblyForm(forms.ModelForm):

    class Meta:
        model = ToolAssembly
        fields = ['tool_nr', 'radius', 'total_length', 'outside_holder', 'machine', 'holder', 'tool']
        labels = {
            'tool_nr': 'Nr narzędzia',
            'radius': 'R',
            'total_length': 'Długość całkowita',
            'outside_holder': 'Długość poza oprawką',
            'machine': 'Maszyna',
            'holder': 'Oprawka',
            'tool': 'Frez',
        }

    def clean(self):
        cleaned_data = super().clean()
        fields_to_check = ['tool_nr', 'radius', 'total_length', 'outside_holder']
        for field_name in fields_to_check:
            field_value = cleaned_data.get(field_name)

            if field_name == 'radius':
                if field_value is not None and (field_value <= 0 or field_value >= 30):
                    self.add_error(field_name, "Promień musi być większy od 0 i mniejszy od 30.")

            elif field_name == 'outside_holder':
                total_length = cleaned_data.get('total_length')
                outside_holder = cleaned_data.get('outside_holder')
                if outside_holder is not None and total_length is not None and outside_holder >= total_length:
                    self.add_error(field_name, "Wartość pola 'Długość poza oprawką' musi być mniejsza niż 'Długość całkowita'.")

            elif field_value is not None and field_value <= 0:
                self.add_error(field_name, f"Wartość {field_name} musi być większa niż 0.")

        return cleaned_data


class ToolAssemblySlim(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['tool_nr'].widget.attrs['disabled'] = 'disabled'
        self.fields['machine'].widget.attrs['disabled'] = 'disabled'
        self.fields['holder'].widget.attrs['disabled'] = 'disabled'
        self.fields['tool'].widget.attrs['disabled'] = 'disabled'

    class Meta:
        model = ToolAssembly
        fields = ['tool_nr', 'radius', 'total_length', 'outside_holder', 'machine', 'holder', 'tool']
        labels = {
            'tool_nr': 'Nr narzędzia',
            'radius': 'R',
            'total_length': 'Długość całkowita',
            'outside_holder': 'Długość poza oprawką',
            'machine': 'Maszyna',
            'holder': 'Oprawka',
            'tool': 'Frez',
        }


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ['content']
        labels = {
            'content': 'Komentarz',
        }

        widgets = {
            'content': forms.Textarea(attrs={'rows': 2}),
        }
