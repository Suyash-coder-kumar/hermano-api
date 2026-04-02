from django.shortcuts import render
from rest_framework import generics,permissions,response
from .serializers import LikeSerializer,CommentSerilaizer,FollowSerializer
from .models import Likes,Comment,Follow
from posts.models import Post
from users.models import User
# Create your views here.

class LikePostView(generics.CreateAPIView):
    serializer_class=LikeSerializer
    permission_class=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        post_id= self.request.data.get('posts')
        post=Post.objects.get(id=post_id)
        serializer.save(user=self.request.user,post=post)

class CommentPostView(generics.CreateAPIView):
    serializer_class=CommentSerilaizer
    permission_classes=[permissions.IsAuthenticated]
    def perform_create(self,serializer):
        post_id= self.request.data.get('posts')
        post=Post.objects.get(id=post_id)
        serializer.save(user=self.request.user,post=post)

class FollowToggleView(generics.GenericAPIView):
    serializer_class=FollowSerializer
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request,user_id):
        follower=request.user
        following=User.objects.get(id=user_id)
        obj,created=Follow.objects.get_or_create(follower=follower,following=following)
        if not created:
            obj.delete()
            return response.Response({'status':"unfollowed"})
        return response.Response({'status':"followed"})
        