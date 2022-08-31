from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    

