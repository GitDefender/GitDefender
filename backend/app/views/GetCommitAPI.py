from rest_framework import viewsets, permissions, generics, status
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated ,BasePermission ,SAFE_METHODS
from rest_framework.response import Response
#from rest_framework.views import ListAPIView

from knox.auth import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token

from ..library.get_commit import crawl_commit
from ..models import GdfUser
import json

# 로직 보여주기 
# 응답할 내용을 적어주기



    # 클래스 > 모든 인스턴스에서 공유되는 모든 attribute와 메서드를 위한것
    #클래스 기반 APIView 사용
   
  
@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([TokenAuthentication])

def get_commit(request, format=None):
        try:
            print("((((((((((((((((()))))))))))))))))")
            models_username = request.user.get_username()
            print("111111111111111111-----------------------")

            user_gdf = GdfUser.objects.get(username=models_username)
            # 유저이름과 일치할때 
            print("22222222222222222222-----------------------")

            user_tok = "Token " + user_gdf.github_token

            get_commit_instance = crawl_commit(user_tok)

            body = get_commit_instance.get_commit()
            print(body)
            return Response(body, status=status.HTTP_200_OK)

        except Exception as e:
            body = dict(
            message=e
                        )
            return Response(body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
