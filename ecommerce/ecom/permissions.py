from rest_framework import permissions

class AdminOrOwner(permissions.BasePermission):
    message = 'you don\'t have enough permissions '
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
    
    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_superuser


class ItemPermission(AdminOrOwner):
    def has_object_permission(self, request, view, obj):
        return obj.cart.user == request.user or request.user.is_superuser

