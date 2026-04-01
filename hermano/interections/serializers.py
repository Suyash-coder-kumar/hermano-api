from rest_framework import serializers
from .models import Likes,Comment,Follow

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Likes
        fields=['id','user','post','created_at']
        read_only_fields=['user','created_at']

class CommentSerilaizer(serializers.ModelSerializer):
    user=serializers.StringRelatedField(read_only=True)
    class Meta:
        model=Comment
        fields=['id','user','post','text','created_at']
        read_only_fields=['user','created_at']

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ['id', 'follower', 'following', 'created_at']
        read_only_fields = ['follower', 'created_at']