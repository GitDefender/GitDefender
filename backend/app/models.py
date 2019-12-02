from django.db import models
from django.contrib.auth.models import User

class GdfUser(models.Model):
    username = models.CharField(max_length=50, blank=False, unique=True, primary_key=True)
    github_token = models.CharField(max_length=50, blank=True, unique=True, null=True)
    gitlab_token = models.CharField(max_length=50, blank=True, unique=True, null=True)
    bitbucket_token = models.CharField(max_length=50, blank=True, unique=True, null=True)