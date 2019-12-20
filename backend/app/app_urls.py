from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import oauth2, RegistrationAPI, LoginAPI, UserAPI, LogoutView, oauth2_callback, GetRepositoryView
from .views import get_branch, get_code_detect
from .views import get_commit


schema_view = get_schema_view(
   openapi.Info(
      title="GitDefender API",
      default_version='v1',
      description="프론트엔드 호출전용 API - 개발이후 CORS 화이트리스트 처리예정",
      terms_of_service="https://gitdefender.com/policies/terms",
      contact=openapi.Contact(email="roharon@studentpartner.com"),
      license=openapi.License(name="MIT License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('auth/oauth2', oauth2, name='oauth2'),
    path('auth/register', RegistrationAPI.as_view(), name='register'),
    path('auth/user', UserAPI.as_view(), name='user'),
    path('auth/login', LoginAPI.as_view(), name='login'),
    path('auth/logout', LogoutView.as_view(), name='logout'),
    path('auth/github_oauth_callback', oauth2_callback, name='github_oauth_calback'),
    path('get_repository', GetRepositoryView.as_view(), name='repository'),
    path('get_commit', get_commit, name='commit'),
    path('get_branch', get_branch, name='branch'),
    path('get_code_detect', get_code_detect, name='codedetect'),
    

    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]