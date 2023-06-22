from rest_framework import serializers
from rest_framework.views import Request, Response, status, APIView
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
    username = serializers.CharField(max_length=150, write_only=True, message={"username": ["This field is required."]})
    password = serializers.CharField(max_length=127, write_only=True,  message={"password": ["This field is required."]})

    #def validate_unique_infos(self, value: User):
    #    email_validation = User.objects.get(self.email)
    #    user_validation = User.objects.get(self.username)
    #    return not email_validation ({"email already registered."}) or not user_validation ({"username already taken."}) or ...
