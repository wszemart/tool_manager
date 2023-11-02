from django import forms
from django.utils.translation import gettext as _

from .models import Tool


class ToolForm(forms.ModelForm):
    class Meta:
        model = Tool
        fields = [
            "tool_type",
            "catalog_nr",
            "R",
            "L1",
            "D1",
            "L2",
            "D2",
            "L3",
            "D3",
            "L4",
            "D4",
        ]
        labels = {
            "tool_type": "Typ freza",
            "catalog_nr": "Nr katalogowy",
        }

    def clean(self):
        cleaned_data = super().clean()
        fields_to_check = ["R", "L1", "D1", "L2", "D2", "L3", "D3", "L4", "D4"]
        for field_name in fields_to_check:
            field_value = cleaned_data.get(field_name)
            if field_value is not None and field_value <= 0:
                self.add_error(field_name, _(f"Value {field_name} have to be more than 0."))

        return cleaned_data
