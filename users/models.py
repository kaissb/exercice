from django.db import models

# Create your models here.
class User(models.Model):
    Name_user = models.CharField(max_length=50)
    Email_user = models.EmailField(max_length=150)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
