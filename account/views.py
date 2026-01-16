from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .serializers import UserRegistrationSerializer, UserLoginSerializer, UserProfileSerializer, UserChangePasswordserializer,  SendPasswordResetEmailSerializer, UserPasswordResetSerializer, UserVerificationEmailSerializer
from django.contrib.auth import authenticate
from .renderers import UserRender
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .utils import Util


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }


class UserRegistrationView(APIView):
    renderer_classes = [UserRender]
    def post(self, request, format=None):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_tokens_for_user(user)
            #Send Email
            Util.send_verification_email(request, user)
            return Response({"token": token, "msg": "Registration success! Please check your email."}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserVerificationEmailView(APIView):
    renderer_classes = [UserRender]
    def get(self, request, uid, token, format=None):
        serializer = UserVerificationEmailSerializer(data={}, context={'uid':uid, 'token':token})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Your Account is activated!"}, status=status.HTTP_200_OK)


class UserLoginView(APIView):
    renderer_classes = [UserRender]
    def post(self, request, format=None):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                token = get_tokens_for_user(user)
                return Response({"token": token, "msg": "Login Successful"}, status=status.HTTP_200_OK)
            else:
                return Response({"errors": {"non_field_errors": ["Email or Password is not Valid"]}}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserProfileView(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]
    def get(self, request, format=None):
        serializer = UserProfileSerializer(request.user)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserChangePasswordView(APIView):
    renderer_classes = [UserRender]
    permission_classes = [IsAuthenticated]
    def post(self, request, format=None):
        serializer = UserChangePasswordserializer(data=request.data, context={'user': request.user})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Change Successfully!"}, status=status.HTTP_200_OK)
    

class SendPasswordResetEmailView(APIView):
    renderer_classes = [UserRender]
    def post(self, request, format=None):
        serializer = SendPasswordResetEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Reset link send. Please check your Email."}, status=status.HTTP_200_OK)
    

class UserPasswordResetView(APIView):
    renderer_classes = [UserRender]
    def post(self, request, uid, token, format=None):
        serializer = UserPasswordResetSerializer(data=request.data, context={'uid': uid, 'token': token})
        serializer.is_valid(raise_exception=True)
        return Response({"msg": "Password Reset Succesfully!"}, status=status.HTTP_200_OK)