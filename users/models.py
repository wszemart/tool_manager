from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import Group


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Profile of {self.user.username}'


programmer_group, created = Group.objects.get_or_create(name='Programmer')
operator_group, created = Group.objects.get_or_create(name='Operator')


