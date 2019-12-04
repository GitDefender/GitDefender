from django.urls import path, include

from .views import oauth2, RegistrationAPI, LoginAPI, UserAPI, LogoutView, oauth2_callback
from .views import get_repo
from .views import get_commit

urlpatterns = [
    path('auth/oauth2/', oauth2, name='oauth2'),
    path('auth/register/', RegistrationAPI.as_view(), name='register'),
    path('auth/user/', UserAPI.as_view(), name='user'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/github_oauth_callback/', oauth2_callback, name='github_oauth_calback'),
    path('auth/get_repository/', get_repo, name='repository'),
    path('auth/get_commit/', get_commit, name='commit'),

]