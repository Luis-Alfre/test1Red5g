from importlib.resources import path
from django.db import router
from .views import commentView
from rest_framework import routers
from django.urls import include, path

router = routers.SimpleRouter()
router.register(r'comment', commentView, basename='comment')

urlpatterns = [
    path('',include(router.urls)),
]

urlpatterns+=router.urls


