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


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = ['tool_type', 'catalog_nr', 'R', 'L1', 'D1', 'L2', 'D2', 'L3', 'D3', 'L4', 'D4']
        labels = {
            'tool_type': 'Typ freza',
            'catalog_nr': 'Nr katalogowy',
        }


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
