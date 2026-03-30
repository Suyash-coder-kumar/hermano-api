from django.urls import path
from .views import RegisterView,ProfileView,UserSearchView
urlpatterns=[
    path('register/',RegisterView.as_view()),
    path('profile/',ProfileView.as_view()),
    path('search/',UserSearchView.as_view())
]