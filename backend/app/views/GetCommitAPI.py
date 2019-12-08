from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from knox.auth import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from app.views import swagger_collection as sche
from app.models import GdfUser
from app.library.get_commit import crawl_commit
from app.library.crawl_tool_base import CrawlTool


test_param = openapi.Parameter('repository_name', openapi.IN_QUERY, description="Github Repository full name", type=openapi.TYPE_STRING)
test_param1 = openapi.Parameter('repository_branch', openapi.IN_QUERY, description="Github Repository branch full name", type=openapi.TYPE_STRING)


@swagger_auto_schema(method='get', manual_parameters=[test_param]and[test_param1], operation_description="GET /api/v1/get_commit",
            responses={
                200: sche.GET_BRANCH_STATUS_200.as_md(),
                401: sche.GET_401.as_md()
            })   
  
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])
@api_view(['GET'])
def get_commit(request, format=None):
        try:
            user_gdf_token = request.headers['Authorization'].replace("Token", "").strip()
            user_repo_name = request.GET['repository_name']
            user_repo_branch = request.GET['repository_branch']

            get_commit_instance = crawl_commit()

            body = get_commit_instance.get_commit(user_gdf_token,user_repo_name,user_repo_branch)
            print(body)
            return Response(body, status=status.HTTP_200_OK)

        except ObjectDoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)
