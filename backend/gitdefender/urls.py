from django.contrib import admin
from django.urls import path, include
from app import app_urls
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(app_urls)),
]
#    path('api-oauth/', include('rest_framework.urls', namespace='rest_framework'))
