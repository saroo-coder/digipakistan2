from rest_framework import permissions
from rest_framework.exceptions import PermissionDenied

class IsClient(permissions.BasePermission):
    def has_permission(self, request, view):
        print("request.user.is_authenticated",request.user.is_authenticated)
        if request.user.is_authenticated:
            print(request.user)
            if request.user.is_client:
                return True
            else:
                raise PermissionDenied('Only client can make this request')
        else:
            raise PermissionDenied('You must be logged in to make this request') 

