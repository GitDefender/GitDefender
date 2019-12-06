from rest_framework import permissions, generics
from knox.auth import TokenAuthentication
from ..serializers import (
    UserSerializer,
)

class UserAPI(generics.RetrieveAPIView):
    authentication_classes = (TokenAuthentication,)     
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user