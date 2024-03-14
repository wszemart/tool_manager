from django import forms
from django.utils.translation import gettext as _

from .models import ToolAssembly, UserComment


class ToolAssemblyForm(forms.ModelForm):
    class Meta:
        model = ToolAssembly
        fields = [
            "tool_nr",
            "radius",
            "total_length",
            "outside_holder",
            "machine",
            "holder",
            "tool",
        ]
        labels = {
            "tool_nr": "Nr narzędzia",
            "radius": "R",
            "total_length": "Długość całkowita",
            "outside_holder": "Długość poza oprawką",
            "machine": "Maszyna",
            "holder": "Oprawka",
            "tool": "Frez",
        }

    def clean_outside_holder(self):
        cleaned_data = super().clean()
        total_length = cleaned_data.get("total_length")
        outside_holder = cleaned_data.get("outside_holder")
        if outside_holder is not None and total_length is not None and outside_holder >= total_length:
            self.add_error(
                "outside_holder",
                _("The length 'outside_holder' value must be smaller than the 'total length'."),
            )

        return outside_holder

    def clean_radius(self):
        cleaned_data = super().clean()
        radius = cleaned_data.get("radius")

        if radius is not None and (radius <= 0 or radius >= 30):
            self.add_error(
                "radius",
                _("The radius must be greater than 0 and less than 30."),
            )

        return radius

    def clean(self):
        cleaned_data = super().clean()
        fields_to_check = ["tool_nr", "total_length", "outside_holder"]
        for field_name in fields_to_check:
            field_value = cleaned_data.get(field_name)

            if field_value is not None and field_value <= 0:
                self.add_error(field_name, _(f"Value {field_name} have to be more than 0."))

        return cleaned_data


class ToolAssemblySlim(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["tool_nr"].disabled = True
        self.fields["machine"].disabled = True
        self.fields["holder"].disabled = True
        self.fields["tool"].disabled = True
        self.fields["tool_nr"].required = False
        self.fields["machine"].required = False
        self.fields["holder"].required = False
        self.fields["tool"].required = False

    class Meta:
        model = ToolAssembly
        fields = [
            "tool_nr",
            "radius",
            "total_length",
            "outside_holder",
            "machine",
            "holder",
            "tool",
        ]
        labels = {
            "tool_nr": "Nr narzędzia",
            "radius": "R",
            "total_length": "Długość całkowita",
            "outside_holder": "Długość poza oprawką",
            "machine": "Maszyna",
            "holder": "Oprawka",
            "tool": "Frez",
        }

    def clean_outside_holder(self):
        cleaned_data = super().clean()
        total_length = cleaned_data.get("total_length")
        outside_holder = cleaned_data.get("outside_holder")
        if outside_holder is not None and total_length is not None and outside_holder >= total_length:
            self.add_error(
                "outside_holder",
                _("The length 'outside_holder' value must be smaller than the 'total length'."),
            )

        return outside_holder

    def clean_radius(self):
        cleaned_data = super().clean()
        radius = cleaned_data.get("radius")

        if radius is not None and (radius <= 0 or radius >= 30):
            self.add_error(
                "radius",
                _("The radius must be greater than 0 and less than 30."),
            )

        return radius

    def clean(self):
        cleaned_data = super().clean()
        fields_to_check = ["total_length", "outside_holder"]
        for field_name in fields_to_check:
            field_value = cleaned_data.get(field_name)

            if field_value is not None and field_value <= 0:
                self.add_error(field_name, _(f"Value {field_name} have to be more than 0."))

        return cleaned_data


class UserCommentForm(forms.ModelForm):
    class Meta:
        model = UserComment
        fields = ["content"]
        labels = {
            "content": _("Comment"),
        }

        widgets = {
            "content": forms.Textarea(attrs={"rows": 2}),
        }
