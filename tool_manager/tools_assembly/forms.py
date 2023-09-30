from django import forms
from .models import ToolAssembly, UserComment


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
