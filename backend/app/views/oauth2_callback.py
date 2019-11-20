from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
#from gitdefender.client import CLIENT_SECRET, CLIENT_ID
import os
import requests, json

@api_view(['GET', 'POST'])
@permission_classes((IsAuthenticated,))
def oauth2_callback(request):
    """
    :param request:
    :return {status:'', code:''}:
    """
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    ACCESS_TOKEN_URL = "https://github.com/login/oauth/access_token"

    try:
        session_code = request.GET['code']
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
        user_access_token = res.json()['access_token']

        user_access_body = dict(code=user_access_token)

        return Response(user_access_body, status=status.HTTP_200_OK)

    except Exception as e:
        body = {'message': e}
        return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
