import email
from django.shortcuts import render
from rest_framework import mixins, viewsets, status

from apps.user.models import User
from apps.user.serializer import UserSerializer

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.authtoken.models import Token


class UserView(mixins.CreateModelMixin,
               viewsets.GenericViewSet):
    
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    @action(detail=False, methods=['post'])
    def login(self, request, *kwar, **kwargs):
        password = request.data['password']
        mail = request.data['mail']
        user = User.objects.filter(mail = mail, password = password)
        if user:
            #Token.objects.get_or_create(user=user)
            return Response(UserSerializer(user, many=True).data)
        return Response(
            status=status.HTTP_404_NOT_FOUND)
        
