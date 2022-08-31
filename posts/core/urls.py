from django.urls import path, include

from core.models import Post
from .views import PostAPIView, PostCommentView

urlpatterns = [
    path('posts/', PostAPIView.as_view(), name='posts'),
    path('post/<str:pk>/', PostCommentView.as_view())
]
