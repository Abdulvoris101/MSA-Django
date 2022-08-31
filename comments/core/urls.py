from django.urls import path, include
from .views import ComentsApiView, PostCommentAPIView

urlpatterns = [
    path('posts/<str:pk>/comments', PostCommentAPIView.as_view() ),
    path('comments/', ComentsApiView.as_view())
]
