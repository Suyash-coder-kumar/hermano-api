from django.db import models
from posts.models import Post
from users.models import User
# Create your models here.

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    created_at=models.DateTimeField(auto_now_add=True)
    text=models.TextField

    def __str__(self):
        return f"{self.user.username} commented on Post {self.post.id}"

    
class Likes(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='likes')
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together=('user','post')

    def __str__(self):
        return f'{self.user.username} liked post {self.post.id}'
    

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('follower', 'following')

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"