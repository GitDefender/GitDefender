from django.db import models
from django.contrib.auth.models import User

class GdfUser(models.Model):
    username = models.CharField(max_length=50, blank=False, unique=True, primary_key=True)
    gitdefender_token = models.CharField(max_length=50, blank=True, null=True, default='NO')

    github_token = models.CharField(max_length=50, blank=True, null=True, default='NO')
    github_username = models.CharField(max_length=50, blank=True, null=True, default='NO')

    gitlab_token = models.CharField(max_length=50, blank=True, null=True, default='NO')
    gitlab_username = models.CharField(max_length=50, blank=True, null=True, default='NO')

    bitbucket_token = models.CharField(max_length=50, blank=True, null=True, default='NO')
    bitbucket_username = models.CharField(max_length=50, blank=True, null=True, default='NO')