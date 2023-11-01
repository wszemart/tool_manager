from django.contrib.auth.models import User
from django.db import models


class Holder(models.Model):
    holder_type_choices = [
        ("type_1", "SLIM_100"),
        ("type_2", "SLIM_150"),
        ("type_3", "SLIM_200"),
        ("type_4", "TERMO_100"),
        ("type_5", "TERMO_150"),
        ("type_6", "TERMO_200"),
        ("type_7", "ER_32"),
        ("type_8", "ER_40"),
        ("type_9", "WELDON_100"),
        ("type_10", "WELDON_150"),
        ("type_11", "WELDON_200"),
        ("type_12", "STYROPIAN"),
        ("type_13", "UCHWYT_76"),
    ]

    holder_type_dict = dict(holder_type_choices)

    holder_type = models.CharField(max_length=100, choices=holder_type_choices, help_text="Holder type")
    inner_diameter = models.PositiveIntegerField(help_text="Inner diameter of the holder")
    catalog_nr = models.CharField(max_length=100, blank=True, help_text="Holder catalog number")
    LH1 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Length of the first holder segment"
    )
    DH1_A = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True,
        help_text="First outside diameter of the first holder segment",
    )
    DH1_B = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True,
        help_text="Second outside diameter of the first holder segment",
    )
    LH2 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Length of the second holder segment"
    )
    DH2 = models.DecimalField(
        max_digits=10,
        decimal_places=3,
        blank=True,
        null=True,
        help_text="Outside diameter of the second holder segment",
    )
    LH3 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Length of the third holder segment"
    )
    DH3 = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Outside diameter of the third holder segment"
    )
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None, help_text="Author of the holder")

    def __str__(self):
        return self.holder_type_dict.get(self.holder_type, "Unknown holder type")
