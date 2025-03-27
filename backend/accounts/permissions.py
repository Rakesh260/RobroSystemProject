from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):
    """Allow only admin users"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'admin'


class IsSupervisor(BasePermission):
    """Allow supervisors and admins"""
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role in ['admin', 'supervisor']
