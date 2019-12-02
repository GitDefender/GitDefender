from rest_framework import generics, permissions
from rest_framework.response import Response

from knox.auth import TokenAuthentication

from ..serializers import (
    UserSerializer,
    GdfUserSerializer
)

class GithubCallbackAPI(generics.GenericAPIView):
    authentication_classes = (
        TokenAuthentication,
    )
    permission_classes = (
        permissions.IsAuthenticated,
    )
    serializer_class = UserSerializer

    def get(self, request, format=None):
        request.data['github_token'] = 'TTTTTTTT'
        # TODO token 추가
        # UserAPI에서와 연동이 안됨
        serializer = GdfUserSerializer(request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.signals)
        