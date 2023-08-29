# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from tools_assembly.models import UserComment
# from .models import Notification, UserNotification
# from django.contrib.auth.models import User
#
#
# @receiver(post_save, sender=UserComment, dispatch_uid="notifications.signals.new_comment_notification")
# def new_comment_notification(sender, instance, created, **kwargs):
#     if created:
#         new_notification = Notification.objects.create(
#             user=instance.author,
#             user_comment=instance,
#             message='New comment!'
#         )
#
#         users_to_notify = User.objects.all()
#
#         for user in users_to_notify:
#             UserNotification.objects.create(user=user, notification=new_notification)

from django.db.models.signals import post_save
from django.dispatch import receiver
from tools_assembly.models import UserComment
from .models import Notification, UserNotification
from django.contrib.auth.models import User


@receiver(post_save, sender=UserComment, dispatch_uid="notifications.signals.new_comment_notification")
def new_comment_notification(sender, instance, created, **kwargs):
    if created:
        new_notification = Notification.objects.create(
            user=instance.author,
            user_comment=instance,
            message='New comment!'
        )

        users_to_notify = User.objects.exclude(pk=instance.author.pk)

        for user in users_to_notify:
            UserNotification.objects.create(user=user, notification=new_notification)
