from django.dispatch import receiver
from .models import Notification, UserNotification
from .signals import new_comment_notification


@receiver(new_comment_notification)
def create_comment_notification(sender, **kwargs):
    comment = kwargs['comment']
    user = kwargs['user']

    message = f"New comment added by {comment.author} on {comment.tool_assembly}"

    Notification.objects.create(user=user, message=message)

