from django import forms
from .models import Machine


class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['name', 'description']
        labels = {
            'name': 'Nazwa maszyny',
            'description': 'Opis maszyny'
        }
