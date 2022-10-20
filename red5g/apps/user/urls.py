from importlib.resources import path
from django.db import router
from .views import UserView
from rest_framework import routers
from django.urls import include, path

router = routers.SimpleRouter()
router.register(r'user', UserView, basename='user')

urlpatterns = [
    path('',include(router.urls)),
]

urlpatterns+=router.urls


