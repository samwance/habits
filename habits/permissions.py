from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    message = "Необходимо иметь права владельца."

    def has_object_permission(self, request, view, obj):
        if hasattr(obj, "user"):
            return request.user == obj.user
        return False
