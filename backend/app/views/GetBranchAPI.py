from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from ..library.get_branch import GetBranch

@permission_classes((IsAuthenticated,))
@api_view(['GET'])
def get_branch(request):
    try:
        user_gdf_token = request.headers['Authorization'].replace("Token", "").strip()
    except ObjectDoesNotExist as e:
        return Response(status.HTTP_401_UNAUTHORIZED)

