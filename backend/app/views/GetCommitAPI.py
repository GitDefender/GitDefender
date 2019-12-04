from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from ..library.get_commit import crawl_commit
from ..models import GdfUser # username 
# repo name 도 가져와야함

import json

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))

def get_commit(request):
    try:
        models_username = request.user.get_username()
        user_gdf = GdfUser.objects.get(username=models_username)
        get_commit_instance = GetRepository(user_gdf.github_token)
        # 커밋내용 가져오기
        
        body = dict(
            get_commit_instance.get_commit
        )

        return Response(body, status=status.HTTP_200_OK)
    except Exception as e:
        body = dict(
            message=e
        )
        return Response(body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
