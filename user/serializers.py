from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from user.models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.CharField(max_length=127, validators=[UniqueValidator(
        queryset=User.objects.all(), message="email already registered.")])
    first_name = serializers.CharField(max_length=50)
    username = serializers.CharField(max_length=20,
                                    validators=[UniqueValidator(queryset=User.objects.all(),
                                                                message="username already taken.")])
    password = serializers.CharField(max_length=50, write_only=True)
    last_name = serializers.CharField(max_length=50)
    birthdate = serializers.DateField(allow_null=True, default=None)
    is_employee = serializers.BooleanField(allow_null=True, default=False)
    is_superuser = serializers.BooleanField(read_only=True)

    def create(self, validated_data: dict) -> User:
        if validated_data["is_employee"]:
            return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=150, write_only=True)
    password = serializers.CharField(max_length=127, write_only=True)
