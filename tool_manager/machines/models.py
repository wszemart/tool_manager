from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Machine(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def get_absolute_url(self):
        return reverse("machine-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.name
