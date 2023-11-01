from django.contrib.auth.models import User
from django.db import models

from tools_assembly.models import UserComment


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Author of the notification")
    user_comment = models.ForeignKey(UserComment, on_delete=models.CASCADE, help_text="User comment")
    message = models.TextField(default="New comment!")
    is_read = models.BooleanField(default=False, help_text="Notification status")
    created_at = models.DateTimeField(auto_now_add=True, help_text="Comment creation date")


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text="Author of the user notification")
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE, help_text="Notification sent to users")
    is_read = models.BooleanField(default=False, help_text="User notification status")
