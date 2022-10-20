from importlib.resources import path
from django.db import router
from .views import newsView
from rest_framework import routers
from django.urls import include, path

router = routers.SimpleRouter()
router.register(r'news', newsView, basename='news')

urlpatterns = [
    path('',include(router.urls)),
]

urlpatterns+=router.urls


