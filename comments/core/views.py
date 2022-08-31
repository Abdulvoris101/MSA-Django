from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CommentSerializer
from .models import Comment
from rest_framework.response import Response


import urllib3
import json

http = urllib3.PoolManager()


class PostCommentAPIView(APIView):
    def get(self, _, pk=None):
        comments = Comment.objects.filter(post_id=pk)
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)
        

class ComentsApiView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        serializer.save()

        data = serializer.data

        self.formatPost(data['post_id'], data['text'])

        return Response(data)
    

    def formatPost(self, post_id, text):

        body = {
            'text': text
        }

        r = http.request('POST', f'http://localhost:8000/api/post/{post_id}/',
                        headers={'Content-Type': 'application/json'},
                        body=json.dumps(body))
        
        