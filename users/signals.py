from django.contrib.auth.models import Group, User
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender: User, instance: User, created: bool, **kwargs) -> None:
    if created:
        Profile.objects.create(user=instance)
        operator, _ = Group.objects.get_or_create(name="Operator")
        instance.groups.add(operator)
        instance.save()
