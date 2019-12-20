from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from knox.auth import TokenAuthentication
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import redirect


from app.views import swagger_collection as sche

@swagger_auto_schema(method='get', manual_parameters=[], operation_description="GET /api/v1/auth/oauth2\nLogin to Github\nJust call, Do not get any response",
            responses={
                401: sche.GET_401.as_md(),
            })
@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def oauth2(request):
    print('------------------------')
    try:
        
        user_gdf_token = request.headers['Authorization'].replace("Token", "").strip()
    except:
        body = dict(message="Please GET with Authorization")
        return Response(body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return redirect("https://github.com/login/oauth/authorize?"\
        "scope=repo%20read:repo_hook%20read:org%20read:user%20user:email%20&" \
        "client_id=d220f1ce704075b77610" \
        "&state=" + user_gdf_token)
