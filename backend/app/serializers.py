from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from .models import GdfUser

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = GdfUser
        fields = ("id", "username", "email", "password")
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data["username"], 
            validated_data["email"], validated_data["password"]
        )
        return user

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")

class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(help_text="your username")
    password = serializers.CharField(help_text="your password")

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Unable to log in with provided credentials")

class GithubSerializer(serializers.Serializer):
    token = serializers.CharField()