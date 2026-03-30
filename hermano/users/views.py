from django.shortcuts import render
from rest_framework import generics,permissions
from .models import User
from .serializers import RegisterSerializer,ProfileSerializer
from django.db.models import Q
# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer

class ProfileView(generics.RetrieveUpdateAPIView):
    serializer_class=ProfileSerializer
    permission_classes=permissions.IsAuthenticated

    def get_object(self):
        return self.request.user
    
class UserSearchView(generics.ListAPIView):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('q', '')
        return User.objects.filter(Q(handel__icontains=query) | Q(email__icontains=query))


