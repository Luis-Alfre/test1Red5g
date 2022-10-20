from pydoc import visiblename
from django.shortcuts import render
from rest_framework import mixins, viewsets

from apps.news.models import News
from apps.news.serializer import newsSerializer



class newsView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               viewsets.GenericViewSet):
    
    queryset = News.objects.all()
    serializer_class = newsSerializer
    