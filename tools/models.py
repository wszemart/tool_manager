from django.contrib.auth.models import User
from django.db import models


class Tool(models.Model):
    tool_type_choices = [
        ("end_mill", "WALEC"),
        ("ball_nose", "KULA"),
        ("bull_nose", "WALEC_Z_R"),
        ("typer_ball_nose", "STOZKOWY"),
        ("engraving", "GRAWERKA"),
        ("drill", "WIERTŁO"),
    ]

    tool_type_dict = dict(tool_type_choices)

    tool_type = models.CharField(max_length=100, choices=tool_type_choices, help_text="Tool type")
    catalog_nr = models.CharField(max_length=100, help_text="Tool catalog number")
    R = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Corner radius of a end- and bull- mill"
    )
    L1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, help_text="Blade length")
    D1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True, help_text="Blade diameter")
    L2 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Length of the first shaft segment"
    )
    D2 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Diameter of the first shaft segment"
    )
    L3 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Length of the second shaft segment"
    )
    D3 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Diameter of the second shaft segment"
    )
    L4 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Length of the third shaft segment"
    )
    D4 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Diameter of the third shaft segment"
    )
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None, help_text="Author of the tool")

    def __str__(self):
        return self.tool_type_dict.get(self.tool_type, "Unknown tool type")
