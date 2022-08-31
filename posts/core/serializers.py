from .models import Post
from rest_framework.serializers import ModelSerializer, SerializerMethodField
import json

class PostSerializer(ModelSerializer):
    comments = SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_comments(self, post):
        return json.loads(post.comments)