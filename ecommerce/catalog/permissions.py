from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdminOrSafe(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        else:
            if request.user.is_authenticated and request.user.is_superuser:
                return True
        return False