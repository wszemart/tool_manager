from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from holders.models import Holder
from machines.models import Machine
from tools.models import Tool


class ToolAssembly(models.Model):
    tool_nr = models.PositiveIntegerField()
    radius = models.DecimalField(max_digits=10, decimal_places=3, blank=True, null=True)
    total_length = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    outside_holder = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    machine = models.ForeignKey(
        Machine,
        on_delete=models.SET_DEFAULT,
        default=None,
        related_name="tools",
        null=True,
    )
    holder = models.ForeignKey(Holder, on_delete=models.CASCADE)
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE)
    author = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        help_text="author of the tool assembly.",
    )

    def get_comments(self):
        return self.comments.order_by("-date_posted")


class UserComment(models.Model):
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    toolassembly = models.ForeignKey(ToolAssembly, on_delete=models.CASCADE, related_name="comments")
