from rest_framework.settings import api_settings
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import GdfUser

class GdfUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GdfUser
        fields = ('github_token', )

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], 
            validated_data["email"], validated_data["password"]
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    git = GdfUserSerializer(many=False, required=False)

    class Meta:
        model = User
        fields = ("id", "username", "git")

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(help_text="your username")
    password = serializers.CharField(help_text="your password")

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials")

class GetRepositorySerializer(serializers.Serializer):
    class RepoField(serializers.DictField):
        name = serializers.CharField(help_text="Repository name")
        url = serializers.CharField(help_text="Repository URL")
        latest_commit = serializers.DateField(format=api_settings.DATE_FORMAT)
        latest_scan = serializers.DateField(format=api_settings.DATE_FORMAT)

    
    repositories = serializers.ListField(required=True, child=RepoField())
    repository_size = serializers.IntegerField(required=True)

    def to_representation(self, instance):
        return instance



class Oauth2Seriailizer(serializers.Serializer):
    code = serializers.CharField(help_text="provided by Github")
    username = serializers.CharField(help_text="Github username provided by Github")

    def to_representation(self, instance):
        return instance

class GetBranchSerializer(serializers.Serializer):
    branches = serializers.ListField(help_text="['master', 'develop', 'feature/~~/~~]")

    def to_representation(self, instance):
        return instance