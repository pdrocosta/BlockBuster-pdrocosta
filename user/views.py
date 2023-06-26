from django.shortcuts import render
from rest_framework.views import APIView, Request, Response
from user.serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from user.models import User
from movies.permissions import IsAdminOrReadOnly

class UserView(APIView):
    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class LoginView(APIView):
    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    def get(self, request: Request, user_id: int) -> Response:
        if request.user.is_superuser or request.user.id == user_id:
            user = get_object_or_404(User, id=user_id)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        return Response(status=403)

    def patch(self, request: Request, user_id: int) -> Response:
        if request.user.is_superuser or request.user.id == user_id:
            user = get_object_or_404(User, id=user_id)
            serializer = UserSerializer(instance=user, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            for key, value in serializer.validated_data.items():
                setattr(user, key, value)
            user.save()

            return Response(data=serializer.data, status=200)
        return Response(status=403)
