from rest_framework.permissions import BasePermission

class IsClient(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'client'

class IsGestionnaire(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'gestionnaire'

class IsSpecialiste(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.role == 'specialiste'
