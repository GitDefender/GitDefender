from rest_framework import viewsets, permissions, generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from knox.auth import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from app.views import swagger_collection as sche
from app.library.get_repository import GetRepository
from app.models import GdfUser
import json

from app.serializers import (
    GetRepositorySerializer
)

class GetRepositoryView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = (TokenAuthentication,)
    serializer_class = GetRepositorySerializer

    test_param = openapi.Parameter('', openapi.IN_QUERY, description="Github Repository full name", type=openapi.TYPE_STRING)

    @swagger_auto_schema(operation_description="GET /api/v1/get_repository",
                responses={
                    200: sche.GET_REPO_STATUS_200.as_md(),
                    403: sche.GET_REPO_STATUS_403.as_md(),
                    404: sche.GET_REPO_STATUS_404.as_md(),
                })
    def get(self,request):
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
