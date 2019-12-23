from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from django.core.exceptions import FieldDoesNotExist
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from ..serializers import Oauth2Seriailizer
from ..models import GdfUser
import os
import requests, json

test_param = openapi.Parameter('code', openapi.IN_QUERY, description="Github User Identify pre_token", type=openapi.TYPE_STRING)
user_response = openapi.Response('response description', Oauth2Seriailizer)

@swagger_auto_schema(method='get', manual_parameters=[test_param], 
    operation_description="GET /api/v1/auth/github_oauth_callback\nGithub Oauth2 후 자동 리다이렉트 되는 API")
@api_view(['GET'])
def oauth2_callback(request):
    """
    :param request:
    :return {status:'', code:''}:
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"

    try:
        session_code = request.GET['code']
        user_gdf_token = request.GET['state']
        # session_code를 ACCESS_TOKEN_URL에 요청해 token으로 exchange
        header = {
            'Accept': 'application/json'
        }
        
        client_key = dict()

        with open(BASE_DIR + "/gitdefender/key.json", "r") as client_key_data:
            client_key = json.loads(client_key_data.read())
        params = {
            'client_id': client_key['CLIENT_ID'],
            'client_secret': client_key['CLIENT_SECRET'],
            'code': session_code,
        }

        res = requests.post(ACCESS_TOKEN_URL, headers=header, params=params)
        
        try:
            user_access_token = res.json()['access_token']
        except:
            if res.json()['error']:
                body = dict(
                    message=res.json()
                )

                return Response(
                    str(res.json()), status=status.HTTP_401_UNAUTHORIZED
            )
        try:
            res_username = requests.get("https://api.github.com/user", headers={'Authorization': "bearer " + user_access_token}).json()
            res_username = res_username['login']
        except:
            return Response(
                    str(res_username.json()), status=status.HTTP_401_UNAUTHORIZED)

        gdf_instance = GdfUser.objects.get(gitdefender_token=user_gdf_token)
        gdf_instance.github_token = user_access_token
        gdf_instance.github_username = res_username
        gdf_instance.save()
        
        print(gdf_instance)

        user_access_body = dict(
            code=gdf_instance.github_token,
            username=gdf_instance.username
            )

        return Response(user_access_body, status=status.HTTP_200_OK)
        # 디버깅용

    except FieldDoesNotExist as e:
        body = {'message': str(res_username)+str(e.with_traceback)}
        return Response(body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    except Exception as e:
        body = {'message': str(res_username)+str(e.with_traceback)}
        return Response(body, status=status.HTTP_500_INTERNAL_SERVER_ERROR)