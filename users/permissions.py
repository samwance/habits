from rest_framework.permissions import BasePermission


class IsActualUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.is_active and request.user == obj:
            return True
        return False
