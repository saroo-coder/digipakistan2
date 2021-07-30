from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import GenericAPIView
from django.core.mail import send_mail
from django.http import HttpResponse
from .utils import Util
from django.shortcuts import redirect

from rest_framework import status, permissions
from .serializers import *
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import serializers
from rest_framework.views import APIView
from .models import *
from rest_framework.parsers import JSONParser,FileUploadParser,MultiPartParser,FormParser
from django.http import Http404
# from superadmin.serializers import UserSerializer, ProfileSerializer
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
import jwt
from django.conf import settings
import socket
socket.getaddrinfo('localhost', 8080)
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
import os
from superadmin.custompermissions import *
from rest_framework.authentication import SessionAuthentication

# Create your views here.
class RegisterView(generics.GenericAPIView):
    parser_classes = (MultiPartParser,FormParser)
    serializer_class = RergisterSerializer

    def post(self, request):
        serializer = RergisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


"""        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",

                "User": serializer.data}, status=status.HTTP_201_CREATED
                )"""

#      return Response({"Errors": serializers.errors}, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    # permission_classes = (IsAuthenticated, TeacherPermission,)
    # authentication_classes = (SessionAuthentication,)

    def post(self, request):
        username = request.data.get('username', None)
        password = request.data.get('password', None)

        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user:
            serializer = UserLoginSerializer(authenticated_user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response("Invalid Credentials", status=status.HTTP_401_UNAUTHORIZED)

"""
class LoginAPIView(generics.GenericAPIView):
    parser_classes = (MultiPartParser,FormParser)
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class UserListView(generics.ListAPIView):
    parser_classes = (MultiPartParser,FormParser)
    queryset = User.objects.all
    serializer_class = UserSerializer

class UserDetalView(generics.RetrieveAPIView):
    parser_classes = (MultiPartParser,FormParser)
    queryset = User.objects.all
    serializer_class = UserSerializer
"""
class emailsubmit(APIView):
    parser_classes = (MultiPartParser,FormParser)
    serializer_class = EmailSerializer
    def post(self, request, format = None):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(request=request).domain
            relativeLink = reverse('password-reset-confirm', kwargs={'uidb64': uidb64, 'token': token})
            redirect_url = serializer.data.get('redirect_url', '')
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hello, \n Use link below to reset your password  \n' + \
                absurl+"?redirect_url="+redirect_url
            data = {'email_body': email_body, 'to_email': user.email, 'email_subject': 'Reset your passsword'}
            Util.send_email(data)

            return HttpResponse('Success')
        else:
            return HttpResponse('Failed')

#            subject = serializer.data.get('subject')
#            message = serializer.data.get('message')
#            rec_email = serializer.data.get('to_email')
#            from_email = settings.EMAIL_HOST_USER,
#            to_list = [rec_email]
#            send_mail(subject,message,'sarooshtahir22@gmail.com',to_list)

class PasswordTokenCheckAPI(generics.GenericAPIView):
    #serializer_class = SetNewPasswordSerializer

    def get(self, request, uidb64, token):

        #redirect_url = request.GET.get('redirect_url')

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = User.objects.get(id=id)
            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)
            return Response({'success': True,'messege':'Valid','uidb64':uidb64, 'token':token}, status.HTTP_200_OK )

        except DjangoUnicodeDecodeError as identifier:
                return Response({'error': 'Token is not valid, please request a new one'}, status=status.HTTP_400_BAD_REQUEST)

class SetNewPasswordAPIView(generics.GenericAPIView):
    parser_classes = (MultiPartParser,FormParser)
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset success'}, status=status.HTTP_200_OK)

class LogoutAPIView(generics.GenericAPIView):
    parser_classes = (MultiPartParser,FormParser)
    serializer_class = LogoutSerializer
    #permission_classes = (IsAuthenticated,)

    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(status=status.HTTP_204_NO_CONTENT)
# class ProfileView(APIView):
#     parser_classes = (MultiPartParser,FormParser)

#     def get(self,request,format = None):
#         data = ProfileModel.objects.all()
#         serializer = ProfileSerializer (data, many = True)
#         return Response(serializer.data,status = status.HTTP_200_OK)

#     def post(self,request, format=None):
#         serializer = ProfileSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status = status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors,status = status.HTTP_400_BAD_REQUEST)

# class DetailProfileView(APIView):
#     parser_classes = (MultiPartParser,FormParser)


#     def get_object(self, pk):
#         try:
#             return ProfileModel.objects.get(id=pk)
#         except ProfileModel.DoesNotExist:
#             raise Http404


#     def get(self, request, pk, format=None):
#         data = self.get_object(pk)
#         serilizer = ProfileSerializer(data)
#         return Response(serilizer.data)

#     def put(self,request,pk):
#         data = self.get_object(pk)
#         serializer = ProfileSerializer(data , data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, pk, format=None):
#         data = self.get_object(pk)
#         data.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleView(APIView):
    parser_classes = (MultiPartParser,FormParser)
    def get(self,request,format = None):
        article = ArticleModel.objects.all()
        serializer = ArticleSerializer(article, many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request, format=None):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)

    permission_class = (permissions.IsAuthenticatedOrReadOnly)
    def perform_create(self, serializer):
        serializer.save(User=self.request.user)
class DetailArticleView(APIView):
    parser_classes = (MultiPartParser,FormParser)

    def get_object(self, pk):
        try:
            return ArticleModel.objects.get(id=pk)
        except ArticleModel.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serilizer = ArticleSerializer(data)
        return Response(serilizer.data)

    def put(self,request,pk):
        data = self.get_object(pk)
        serializer = ArticleSerializer(data , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    permission_class = (permissions.IsAuthenticatedOrReadOnly)
class RoleView(APIView):
    parser_classes = (MultiPartParser,FormParser)
    def get(self,request,format = None):
        article = RoleModel.objects.all()
        serializer = RoleSerializer(article, many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request, format=None):
        serializer = RoleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)


class DetailRoleView(APIView):
    parser_classes = (MultiPartParser,FormParser)

    def get_object(self, pk):
        try:
            return RoleModel.objects.get(id=pk)
        except RoleModel.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serilizer = RoleSerializer(data)
        return Response(serilizer.data)

    def put(self,request,pk):
        data = self.get_object(pk)
        serializer = RoleSerializer(data , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class OnlineTestView(APIView):
    parser_classes = (MultiPartParser,FormParser)

    def get(self,request,format = None):
        data = OnlineTestModel.objects.all()
        serializer = OnlineTestSerializer(data, many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request, format=None):
        serializer = OnlineTestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)
class DetailOnlineTestModel(APIView):
    parser_classes = (MultiPartParser,FormParser)


    def get_object(self, pk):
        try:
            return OnlineTestModel.objects.get(id=pk)
        except OnlineTestModel.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serilizer = OnlineTestSerializer(data)
        return Response(serilizer.data)

    def put(self,request,pk):
        data = self.get_object(pk)
        serializer = OnlineTestSerializer(data , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


def __str__(self):
    return self.title


class AnnouncementView(APIView):
    parser_classes = (MultiPartParser,FormParser)

    def get(self,request,format = None):
        data = AnnouncementModel.objects.all()
        serializer = AnnouncementSerializer(data, many = True)
        return Response(serializer.data,status = status.HTTP_200_OK)

    def post(self,request, format=None):
        serializer = AnnouncementSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status = status.HTTP_201_CREATED)
        else:
            return Response(serializer.data,status = status.HTTP_400_BAD_REQUEST)

class DetailAnnouncementView(APIView):
    parser_classes = (MultiPartParser,FormParser)


    def get_object(self, pk):
        try:
            return AnnouncementModel.objects.get(id=pk)
        except AnnouncementModel.DoesNotExist:
            raise Http404


    def get(self, request, pk, format=None):
        data = self.get_object(pk)
        serilizer = AnnouncementSerializer(data)
        return Response(serilizer.data)

    def put(self,request,pk):
        data = self.get_object(pk)
        serializer = AnnouncementSerializer(data , data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
