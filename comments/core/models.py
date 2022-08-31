from django.db import models

class Comment(models.Model):
    post_id = models.IntegerField()
    text = models.TextField()
    
