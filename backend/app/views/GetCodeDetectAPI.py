import re

from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from knox.auth import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from app.views import swagger_collection as sche
from app.models import GdfUser
from app.library.get_branch import GetBranch
from app.library.code_detect import GetCodeDetect

test_param = [
    openapi.Parameter('repository_name', openapi.IN_QUERY, description="Github Repository's Full name", type=openapi.TYPE_STRING),
    openapi.Parameter('branch', openapi.IN_QUERY, description="Github Repository's Branch", type=openapi.TYPE_STRING),
    openapi.Parameter('commit_sha', openapi.IN_QUERY, description="Github Repository's Commit SHA", type=openapi.TYPE_STRING),
]

@swagger_auto_schema(method='get', manual_parameters=test_param, operation_description="GET /api/v1/get_code_detect",
            responses={
                200: sche.GET_CODE_DETECT_STATUS_200.as_md(),
                401: sche.GET_401.as_md(),
            })
@api_view(['GET'])
@permission_classes((IsAuthenticated,))
@authentication_classes([TokenAuthentication])
def get_code_detect(request):
    user_gdf_token = request.headers['Authorization'].replace("Token", "").strip()
    # user gitdefender token

    if re.match("[A-za-z0-9]+(?:[._-][a-z0-9]+)*", request.GET['repository_name']) is None:
        return Response(dict(message="BAD REPO NAME"), status=status.HTTP_400_BAD_REQUEST)
    else:
        select_repo_name = request.GET['repository_name']
    
    # target repository name
    try:
        branch = request.GET['branch'].replace('&&','').replace(";", "").strip()
    except:
        branch = "master"
        
    try:
        commit_sha = request.GET['commit_sha'].replace('&&','').replace(";", "").strip()
        # target repo commit
    except:
        commit_sha = None
        
    gcd_instance = GetCodeDetect(user_gdf_token, select_repo_name, branch, commit_sha)
    result = gcd_instance.detect()

    
    return Response(result, status=status.HTTP_200_OK)