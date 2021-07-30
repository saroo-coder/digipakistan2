from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsStudent(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_student:
                return True
            else:
                raise PermissionDenied('Only student can make this request')
        else:
            raise PermissionDenied('You must be logged in to make this request') 