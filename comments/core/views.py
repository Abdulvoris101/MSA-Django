from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CommentSerializer
from .models import Comment
from rest_framework.response import Response

class ComentsApiView(APIView):
    def get(self, request):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)

        return Response(serializer.data)
    
    def post(self, request):
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)