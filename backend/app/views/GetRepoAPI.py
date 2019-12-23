from rest_framework import viewsets, permissions, generics, status
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from knox.auth import TokenAuthentication
from app.views import swagger_collection as sche
from app.library.get_repository import GetRepository
from app.models import GdfUser
import json

from app.serializers import (
    GetRepositorySerializer
)


class GetRepositoryView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    serializer_class = GetRepositorySerializer

    test_param = [
        openapi.Parameter('page', openapi.IN_QUERY, description="Github Repository page", type=openapi.TYPE_STRING),
        openapi.Parameter('per_page', openapi.IN_QUERY, description="Github Repository amount of a page", type=openapi.TYPE_STRING)
    ]

    @swagger_auto_schema(operation_description="GET /api/v1/get_repository", manual_parameters=test_param,
                responses={
                    200: sche.GET_REPO_STATUS_200.as_md(),
                    401: sche.GET_401.as_md(),
                    404: sche.GET_REPO_STATUS_404.as_md(),
                })
    def get(self,request):
        try:
            models_username = request.user.get_username()
            user_gdf_token = request.headers['Authorization'].replace("Token", "").strip()

            page = request.GET.get('page', 1)
            per_page = request.GET.get('per_page', 10)

            user_gdf = GdfUser.objects.get(gitdefender_token=user_gdf_token)

            user_tok = "Token " + user_gdf.github_token

            get_repo_instance = GetRepository(param_github_tok=user_tok, page=page, per_page=per_page)

            body = get_repo_instance.get_repo()

            return Response(body, status=status.HTTP_200_OK)

        except ObjectDoesNotExist as e:
            body = dict(
                message=e
            )
            return Response(json.dumps(body), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        except Exception as e:
            body = dict(
                message=e
            )

            return Response(json.dumps(body), status=status.HTTP_500_INTERNAL_SERVER_ERROR)