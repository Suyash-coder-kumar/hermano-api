from django.urls import path
from rest_framework import routers
from .views import PostViewset,PostSearchView

router=routers.DefaultRouter()
router.register(r'',PostViewset,basename='posts')

urlpatterns=router.urls

urlpatterns+=[
    path('search/',PostSearchView.as_view(),name='post_search'),
]