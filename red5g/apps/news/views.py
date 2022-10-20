from pydoc import visiblename
from django.shortcuts import render
from rest_framework import mixins, viewsets

from apps.news.models import News
from apps.news.serializer import newsSerializer
from rest_framework.permissions import IsAuthenticated  
from rest_framework.authentication import SessionAuthentication, BasicAuthentication



class newsView(mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.DestroyModelMixin,
               mixins.UpdateModelMixin,
               viewsets.GenericViewSet):
    #rauthentication_classes = [SessionAuthentication, BasicAuthentication]
    # pemission_classes = (IsAuthenticated,)             # <
    queryset = News.objects.all()
    serializer_class = newsSerializer
    