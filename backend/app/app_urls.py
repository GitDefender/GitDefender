from django.urls import path, include
from knox.views import LogoutView
from app import views

from .views import RegistrationAPI, LoginAPI, UserAPI


urlpatterns = [
    path('oauth2/', views.oauth2, name='oauth2'),
    path('auth/register/', RegistrationAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/user/', UserAPI.as_view(), name='user'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
]