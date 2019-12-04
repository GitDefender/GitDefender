from rest_framework import viewsets, permissions, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.signals import user_logged_out
from django.contrib.auth.models import User
from knox.models import AuthToken
from knox.auth import TokenAuthentication

from ..models import GdfUser    
from ..serializers import (
    CreateUserSerializer,
    UserSerializer,
    LoginUserSerializer,
    GdfUserSerializer,
)

class LoginAPI(generics.GenericAPIView):
    permission_classes = [permissions.BasePermission]
    serializer_class = LoginUserSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
            }
        )

class LogoutView(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    serializer_class = LoginUserSerializer
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        body = {"message": "logout successful"}
        return Response(body, status=status.HTTP_200_OK)

class RegistrationAPI(generics.GenericAPIView):
    permission_classes = [permissions.BasePermission]
    serializer_class = CreateUserSerializer

    username_least = 7
    password_least = 8

    def post(self, request, *args, **kwargs):
        try:
            username_short = True if len(request.data["username"]) < self.username_least else False
            password_short = True if len(request.data["password"]) < self.password_least else False
        except:
            body = {"message": "username or password not exist"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)

        if username_short and password_short:
            body = {"message": "short username and password"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        elif username_short:
            body = {"message": "short username"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        elif password_short:
            body = {"message": "short password"}
            return Response(body, status=status.HTTP_400_BAD_REQUEST)
        serializer = self.get_serializer(data = request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        GdfUser.objects.create(username=request.data["username"], gdf_token=AuthToken.objects.create(user)[1])

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
                #(instance, token)
            }
        )