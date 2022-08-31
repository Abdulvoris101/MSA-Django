from django.urls import path, include

from core.models import Post
from .views import PostAPIView

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='posts')
]
