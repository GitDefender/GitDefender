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
from app.library.get_branch import GetBranch

test_param = openapi.Parameter('repository_name', openapi.IN_QUERY, description="Github Repository full name", type=openapi.TYPE_STRING)

@swagger_auto_schema(method='get', manual_parameters=[test_param], operation_description="GET /api/v1/get_branch",
            responses={
                200: sche.GET_BRANCH_STATUS_200.as_md(),
                401: sche.GET_401.as_md()
            })
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def get_branch(request):
    try:
        user_gdf_token = request.headers['Authorization'].replace("Token", "").strip()

        get_branch_instance = GetBranch(user_gdf_token, "Huformation")
        
        body = get_branch_instance.get_branch
        return Response(body, status=status.HTTP_200_OK)

    except ObjectDoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response(str(e), status.HTTP_500_INTERNAL_SERVER_ERROR)
