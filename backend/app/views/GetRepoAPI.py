from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..library.get_repository import GetRepository
from ..models import GdfUser

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def get_repo(request):
    try:
        models_username = request.user.get_username()
        user_gdf = GdfUser.objects.get(username=models_username)
        get_repo_instance = GetRepository(user_gdf.github_token)

        body = dict(
            get_repo_instance.get_repo
        )

        return Response(body, status=status.HTTP_200_OK)
    except Exception as e:
        body = dict(
            message=e
        )
        return Response(body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)