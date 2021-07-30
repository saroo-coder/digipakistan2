from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from allauth.account.adapter import get_adapter
from allauth.account.utils import setup_user_email
from django.contrib.auth import get_user_model, authenticate
from rest_framework.exceptions import PermissionDenied
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from client.models import *

User = get_user_model()

def get_user_from_token(request):
    '''It will given the current username by using token'''
    token = request.user.auth_token
    user = User.objects.get(id=token.user_id)
    return user

class ClientRegistrationSerializer(serializers.ModelSerializer,RegisterSerializer):
    client = serializers.PrimaryKeyRelatedField(read_only=True,)

    class Meta:
        model = ClientModel
        fields = '__all__'

    def get_cleaned_data(self): #customization of rest_auth library code
            data = super(ClientRegistrationSerializer, self).get_cleaned_data()
            extra_data = {
                'name': self.validated_data.get('name', ''),
                'email' : self.validated_data.get('email', ''),
                'password_at_time_of_creation' : self.validated_data.get('password_at_time_of_creation', ''),
                }
            data.update(extra_data)
            print(data)
            return data

    def save(self, request): #from rest_auth library code
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        setup_user_email(request, user, [])
        user.is_client = True
        user.save()
        try:
                client = ClientModel(client=user, name=self.cleaned_data.get('name'),
                    email=self.cleaned_data.get('email'),
                    password_at_time_of_creation=self.cleaned_data.get('password_at_time_of_creation'))
                client.save()
                return user
        except Exception as e:
                print("Eception", e)
                user.delete()
                print("delete user")
                # return Response({'message':'Some thing went wrong. Please try again'}, status=HTTP_400_BAD_REQUEST)
                raise PermissionDenied("Some thing went wrong")


class ClientProfileSerializer(serializers.ModelSerializer):
    client = serializers.SerializerMethodField()

    class Meta:
        model = ClientModel
        fields = ['client', 'name']

    def get_client(self,obj):
        return {
            "Client email": obj.client.email,
            "Client" : obj.client.is_client
            }