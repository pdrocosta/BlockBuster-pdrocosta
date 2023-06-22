from django.shortcuts import render
from rest_framework.views import APIView, Request, Response, status
from user.serializers import UserSerializer, LoginSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.views import TokenObtainPairView

permission_classes=[]

class UserView(APIView):

    def post(self, request: Request) -> Response:
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class LoginView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request: Request) -> Response:
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(**serializer.validated_data)

        if not user:
            return Response({"detail": "No active account found with the given credentials"}, status=400)
        refresh = RefreshToken.for_user(user)
        token_dict = {"refresh": str(refresh),
                      "access": str(refresh.access_token)}
        return Response(token_dict, status=200)
