from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from tools_assembly.models import UserComment


class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(UserComment, on_delete=models.CASCADE)
    message = models.TextField(default='New comment!')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


class UserNotification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    notification = models.ForeignKey(Notification, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
