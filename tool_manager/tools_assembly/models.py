from django.db import models
from machines.models import Machine
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.utils import timezone


class Holder(models.Model):
    holder_type_choices = [
        ('type_1', 'SLIM_100'),
        ('type_2', 'SLIM_150'),
        ('type_3', 'SLIM_200'),
        ('type_4', 'TERMO_100'),
        ('type_5', 'TERMO_150'),
        ('type_6', 'TERMO_200'),
        ('type_7', 'ER_32'),
        ('type_8', 'ER_40'),
        ('type_9', 'WELDON_100'),
        ('type_10', 'WELDON_150'),
        ('type_11', 'WELDON_200'),
        ('type_12', 'STYROPIAN'),
        ('type_13', 'UCHWYT_76'),
    ]

    holder_type_dict = dict(holder_type_choices)

    holder_type = models.CharField(max_length=100, choices=holder_type_choices)
    inner_diameter = models.PositiveIntegerField()
    catalog_nr = models.CharField(max_length=100, blank=True)
    LH1 = models.FloatField(blank=True, null=True)
    DH1_A = models.FloatField(blank=True, null=True)
    DH1_B = models.FloatField(blank=True, null=True)
    LH2 = models.FloatField(blank=True, null=True)
    DH2 = models.FloatField(blank=True, null=True)
    LH3 = models.FloatField(blank=True, null=True)
    DH3 = models.FloatField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.holder_type_dict.get(self.holder_type, 'Unknown holder type')


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
    R = models.PositiveIntegerField(blank=True, null=True)
    L1 = models.FloatField(blank=True, null=True)
    D1 = models.FloatField(blank=True, null=True)
    L2 = models.FloatField(blank=True, null=True)
    D2 = models.FloatField(blank=True, null=True)
    L3 = models.FloatField(blank=True, null=True)
    D3 = models.FloatField(blank=True, null=True)
    L4 = models.FloatField(blank=True, null=True)
    D4 = models.FloatField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

    def __str__(self):
        return self.tool_type_dict.get(self.tool_type, 'Unknown tool type')


class ToolAssembly(models.Model):
    tool_nr = models.IntegerField()
    radius = models.FloatField()
    total_length = models.FloatField()
    outside_holder = models.FloatField()
    machine = models.ForeignKey(Machine, on_delete=models.SET_DEFAULT, default=None, related_name='tools') #zrobić, żeby sie nie kasowało! # machine.tools
    holder = models.ForeignKey(Holder, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)

    def get_comments(self):
        return self.comments.order_by('-date_posted')

    # def clean(self):
    #     super().clean()
    #     fields_to_check = ['tool_nr', 'radius', 'total_length', 'outside_holder']
    #     for field_name in fields_to_check:
    #         field_value = getattr(self, field_name)
    #         if field_value is not None and field_value <= 0:
    #             raise ValidationError(f"{field_name} musi być większe niż 0. wiadomosc z models")
    #
    # def save(self, *args, **kwargs):
    #     self.clean()
    #     super().save(*args, **kwargs)


class UserComment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default=None)
    toolassembly = models.ForeignKey(ToolAssembly, on_delete=models.CASCADE, related_name='comments')
