from rest_framework import serializers, status, exceptions
from django.contrib.auth.models import User

class UserConfirmSerializer(serializers.Serializer):
    username = serializers.CharField()
    code = serializers.IntegerField()


class UserAuthSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


class UserCreateSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate_username(self, username):
        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username
        raise exceptions.ValidationError('User already exists!')