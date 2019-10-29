from rest_framework import routers
from django.urls import path, include
from app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

urlpatterns = [
    path('oauth2/', views.oauth2),
    path('', include(router.urls)),
]