from django.shortcuts import render
from rest_framework import mixins, viewsets

from apps.comment.models import Comment
from apps.comment.serializer import commentSerializer

# Create your views here.

class commentView(mixins.CreateModelMixin,
                  mixins.ListModelMixin,
                  viewsets.GenericViewSet):
    
    queryset = Comment.objects.all()
    serializer_class = commentSerializer
    
