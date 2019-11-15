from django.db import models
from django.contrib.auth.models import User

class GdfUser(models.Model):
    length = 50
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='git')
    github_token = models.CharField(max_length=length, blank=True)
    gitlab_token = models.CharField(max_length=length, blank=True)
    bitbucket_token = models.CharField(max_length=length, blank=True)