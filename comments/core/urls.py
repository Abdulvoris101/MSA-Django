from django.urls import path, include
from .views import ComentsApiView

urlpatterns = [
    path('comments/', ComentsApiView.as_view())
]
