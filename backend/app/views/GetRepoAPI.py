from rest_framework import viewsets, permissions, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.auth import TokenAuthentication

from ..library.get_repository import GetRepository
from ..models import GdfUser
import json

from ..serializers import (
    GetRepositorySerializer
)

class GetRepositoryView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    serializer_class = GetRepositorySerializer

    def get(self,request, *args, **kwargs):
        try:
            models_username = request.user.get_username()
            user_gdf = GdfUser.objects.get(username=models_username)

            user_tok = "Token " + user_gdf.github_token
            get_repo_instance = GetRepository(user_tok)

            body = get_repo_instance.get_repo()

            return Response(body, status=status.HTTP_200_OK)

        except Exception as e:
            body = dict(
                message=e
            )

            return Response(body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
