from django.shortcuts import render
from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

import urllib3
import json

http = urllib3.PoolManager()






class PostAPIView(APIView):
    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response(self.formatPost(p) for p in posts)
    
    def formatPost(self, post):
        
        r = http.request('GET', f'http://localhost:8001/api/posts/{post.id}/comments')
        
        return {
            'id': post.id,
            'title': post.title,
            'description': post.description,
            'comments': json.loads(r.data.decode('utf-8'))
        }

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    

