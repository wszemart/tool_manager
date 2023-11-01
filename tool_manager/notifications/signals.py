from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from tools_assembly.models import UserComment

from .models import Notification, UserNotification


@receiver(
    post_save,
    sender=UserComment,
    dispatch_uid="notifications.signals.new_comment_notification",
)
def new_comment_notification(sender, instance, created, **kwargs):
    if created:
        new_notification = Notification.objects.create(
            user=instance.author,
            user_comment=instance,
            message=f"New comment added by {instance.author}!",
        )

        users_to_notify = User.objects.exclude(pk=instance.author.pk)

        user_notifications_to_create = [
            UserNotification(user=user, notification=new_notification) for user in users_to_notify
        ]

        UserNotification.objects.bulk_create(user_notifications_to_create)
