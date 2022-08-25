from rest_framework import permissions


class IsRestaurant(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'employeerestaurant')


class IsCompany(permissions.BasePermission):
    def has_permission(self, request, view):
        return hasattr(request.user, 'employeecompany')
