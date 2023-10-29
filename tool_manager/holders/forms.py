from django import forms

from .models import Holder


class HolderForm(forms.ModelForm):
    class Meta:
        model = Holder
        fields = [
            "holder_type",
            "inner_diameter",
            "catalog_nr",
            "LH1",
            "DH1_A",
            "DH1_B",
            "LH2",
            "DH2",
            "LH3",
            "DH3",
        ]
        labels = {
            "holder_type": "Typ oprawki",
            "catalog_nr": "Nr katalogowy",
            "inner_diameter": "Średnica wewnętrzna",
        }

    def clean(self):
        cleaned_data = super().clean()
        fields_to_check = [
            "inner_diameter",
            "LH1",
            "DH1_A",
            "DH1_B",
            "LH2",
            "DH2",
            "LH3",
            "DH3",
        ]
        for field_name in fields_to_check:
            field_value = cleaned_data.get(field_name)
            if field_value is not None and field_value <= 0:
                self.add_error(field_name, f"Wartość {field_name} musi być większa niż 0.")

        return cleaned_data
