from django.contrib.auth.models import User
from rest_framework import authentication
from rest_framework import exceptions
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import Group
from rest_framework.exceptions import PermissionDenied

class SuperAdminOrTeacherPermission(BasePermission):

    message = 'Only registered user or superadmin can access APIs'
    group_name = ""
    def has_permission(self, request, view):
        try:
            if(request.user.groups.filter(name__in =['superadmin' , 'teacher'])):
                group_name = request.user.groups.values_list('name',flat=True)
                if ((group_name[0] == 'superadmin') or (group_name[0] == 'teacher')):
                    return group_name
            else:
                return False
        except Group.DoesNotExist:
            self.message = "Permission denied, user not registered!"
        return self.group_name


class SuperAdminPermission(BasePermission):
    message = 'Only registered user or superadmin can access APIs'
    group_name = ""
    def has_permission(self, request, view):
        try:
            if (request.user.groups.get (name = 'superadmin')):
                group_name = 'superadmin'
                return True
        except Group.DoesNotExist:
            self.message = "Permission denied, user not registered!"
        return self.group_name

class SuperAdminOrStudentPermission(BasePermission):

    message = 'Only registered user or superadmin can access APIs'
    group_name = ""
    def has_permission(self, request, view):
        try:
            if(request.user.groups.filter(name__in =['superadmin' , 'student'])):
                group_name = request.user.groups.values_list('name',flat=True)
                if ((group_name[0] == 'superadmin') or (group_name[0] == 'student')):
                    return group_name
            else:
                return False
        except Group.DoesNotExist:
            self.message = "Permission denied, user not registered!"
        return self.group_name

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            else:
                raise PermissionDenied('Only Superuser can make this request')
        else:
            raise PermissionDenied('You must be logged in to make this request') 



class IsStudentORClient(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_student or request.user.is_client:
                return True
            else:
                raise PermissionDenied('Only Student or Client can make this request')
        else:
            raise PermissionDenied('You must be logged in to make this request') 