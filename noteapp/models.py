from pickle import TRUE
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length= 200)
    content = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['created_at']