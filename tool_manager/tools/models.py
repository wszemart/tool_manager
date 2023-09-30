from django.db import models
from machines.models import Machine
from django.contrib.auth.models import User


class Tool(models.Model):
    tool_type_choices = [
        ('end_mill', 'WALEC'),
        ('ball_nose', 'KULA'),
        ('bull_nose', 'WALEC_Z_R'),
        ('typer_ball_nose', 'STOZKOWY'),
        ('engraving', 'GRAWERKA'),
        ('drill', 'WIERTŁO'),
    ]

    tool_type_dict = dict(tool_type_choices)

    tool_type = models.CharField(max_length=100, choices=tool_type_choices)
    catalog_nr = models.CharField(max_length=100)
    R = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    L1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    D1 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    L2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    D2 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    L3 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    D3 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    L4 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    D4 = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.tool_type_dict.get(self.tool_type, 'Unknown tool type')
