from rest_framework import viewsets, permissions, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.signals import user_logged_out
from django.shortcuts import redirect
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from rest_framework.response import Response
from .serializers import (
    CreateUserSerializer,
    UserSerializer,
    LoginUserSerializer,
    GdfUserSerializer
)
from knox.models import AuthToken
from knox.auth import TokenAuthentication
from django.contrib.auth.models import User

from app.library.get_repository import GetRepository
from app.library.crawl_tool_base import CrawlTool

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

        return Response(
            {
                "user": UserSerializer(
                    user, context=self.get_serializer_context()
                ).data,
                "token": AuthToken.objects.create(user)[1],
                #(instance, token)
            }
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

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class LogoutView(generics.GenericAPIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        request._auth.delete()
        user_logged_out.send(sender=request.user.__class__,
                             request=request, user=request.user)
        body = {"message": "logout successful"}
        return Response(body, status=status.HTTP_200_OK)

class GithubCallbackAPI(generics.GenericAPIView):
    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = UserSerializer

    def get(self, request, format=None):
        request.data['github_token'] = 'TTTTTTTT'
        # TODO token 추가
        # UserAPI에서와 연동이 안됨
        serializer = GdfUserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.signals)
        
@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def scan_repo(request):
    gr = GetRepository()
    gr.user_agent = "GitDefender"
    gr.user_token = "Token 6d24306bc3194fd1f11d5f03e8423eb8356fc7d6"
    repo = gr.get_repo()
    return Response(repo)

@csrf_protect
def oauth2(request):
    return redirect("https://github.com/login/oauth/authorize?scope=repo:status%20read:repo_hook%20read:org%20read:user%20user:email%20&client_id=d220f1ce704075b77610")