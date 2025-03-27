
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User, UserImage, ActivityLog
from .serializers import UserSerializer, UserImageSerializer
from .permissions import IsAdmin
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny


class RegisterUserView(APIView):
    permission_classes = [AllowAny]

    """Register a new user"""
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response({'message': 'User registered successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomTokenObtainPairView(TokenObtainPairView):
    """JWT Authentication API"""
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return Response({"token": response.data['access'], "refresh": response.data['refresh']}, status=status.HTTP_200_OK)


class ListCreateUserView(APIView):
    """Admin: Create new Supervisor or Worker"""
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        if request.data.get("role") == "admin":
            return Response({"error": "Cannot create an admin user"}, status=status.HTTP_400_BAD_REQUEST)

        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            ActivityLog.objects.create(user=request.user, action=f"Created new user {user.username} ({user.role})")

            return Response({"message": "User created successfully", "user": serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

