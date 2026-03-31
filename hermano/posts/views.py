from django.shortcuts import render
from rest_framework import viewsets,permissions,generics
from .models import Post
from .serializers import PostSerializer
# Create your views here.

class PostViewset(viewsets.ModelViewSet):
    queryset=Post.objects.all().order_by('-created_at')
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    

class PostSearchView(generics.ListAPIView):
    serializer_class=PostSerializer
    permission_classes=[permissions.IsAuthenticated]

    def get_queryset(self):
        query=self.request.query_params.get('q','')
        return Post.objects.filter(caption__icontains=query).order_by('-created_at')