from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from holders.models import Holder
from machines.models import Machine
from tools.models import Tool


class ToolAssembly(models.Model):
    tool_nr = models.PositiveIntegerField(help_text="Number of the tool assembly in machine table.")
    radius = models.DecimalField(
        max_digits=10, decimal_places=3, blank=True, null=True, help_text="Radius of the tool assembly."
    )
    total_length = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, help_text="Total tool length."
    )
    outside_holder = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True, help_text="Length outside the holder."
    )
    machine = models.ForeignKey(
        Machine,
        on_delete=models.SET_DEFAULT,
        default=None,
        related_name="tools",
        null=True,
        help_text="The machine to which the tool is assigned.",
    )
    holder = models.ForeignKey(
        Holder, on_delete=models.CASCADE, help_text="A holder component used in a tool assembly."
    )
    tool = models.ForeignKey(Tool, on_delete=models.CASCADE, help_text="A tool component used in a tool assembly.")
    author = models.ForeignKey(
        User,
        on_delete=models.SET_DEFAULT,
        default=None,
        help_text="Author of the tool assembly.",
    )

    def get_comments(self):
        return self.comments.order_by("-date_posted")


class UserComment(models.Model):
    content = models.TextField(help_text="User comment.")
    date_posted = models.DateTimeField(
        default=timezone.now, help_text="Date the comment was published <em>YYYY-MM-DD</em>."
    )
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, help_text="Author of the user comment.")
    tool_assembly = models.ForeignKey(
        ToolAssembly,
        on_delete=models.CASCADE,
        related_name="comments",
        help_text="The tool assembly to which the comment is assigned.",
    )
