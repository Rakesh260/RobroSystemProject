
from .models import User, UserImage

from rest_framework import serializers

from .models import ActivityLog, DashboardSummary


class UserSerializer(serializers.ModelSerializer):
    """Serializer for User model"""

    class Meta:
        model = User
        fields = ['id', 'username', 'role', 'password', 'email']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        """Create user with hashed password"""
        user = User.objects.create_user(**validated_data)
        return user


class UserImageSerializer(serializers.ModelSerializer):
    """Serializer for User Image model"""

    class Meta:
        model = UserImage
        fields = ['id', 'user', 'image', 'timestamp']
        extra_kwargs = {'user': {'read_only': True}}


class AssignRoleSerializer(serializers.ModelSerializer):
    """Serializer to update user role"""
    class Meta:
        model = User
        fields = ['role']


class ActivityLogSerializer(serializers.ModelSerializer):
    """Serializer for activity logs"""
    class Meta:
        model = ActivityLog
        fields = '__all__'


class DashboardSummarySerializer(serializers.ModelSerializer):
    """Serializer for dashboard statistics"""
    class Meta:
        model = DashboardSummary
        fields = '__all__'

