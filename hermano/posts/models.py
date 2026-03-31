from django.db import models
from users.models import User
# Create your models here.

class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="posts")
    media=models.FileField(upload_to='posts/')
    created_at=models.DateTimeField(auto_now=True)
    caption=models.TextField()
