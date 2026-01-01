from django.db import models
from django.contrib.auth.models import User

# todo/models.py

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)  # allow null
    title = models.CharField(max_length=255)
    completed = models.BooleanField(default=False)
