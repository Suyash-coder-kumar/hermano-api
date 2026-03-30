from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(blank=True, null=True)
    dp = models.ImageField(blank=True, null=True)
    handle = models.CharField(unique=True, max_length=50, editable=False)

    def save(self, *args, **kwargs):
        if not self.handle: 
            self.handle = f"@{self.username}_hermano"
        super().save(*args, **kwargs) 