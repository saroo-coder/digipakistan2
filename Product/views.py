from django.shortcuts import render
from django.http import Http404
from rest_framework.parsers import JSONParser
from .serializers import *
from .models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status




# Create your views here.

class Product(APIView):
    def get(self,request,format=None):
        data = ProductModel.objects.all()
        serializer = ProductSerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,format=None):
        data = JSONParser().parse(request)
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        else:
            serializer = ProductSerializer()
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)   

class ProductDetail(APIView):
    def get_object(self,pk):
        try:
            return ProductModel.objects.filter(pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        print(pk)
        data = self.get_object(pk)
        serializer = ProductSerializer(data)
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)


class Catagory(APIView):
    def get(self,request,format=None):
        data = CatagoryModel.objects.all()
        serializer = CatagorySerializer(data, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self,request,format=None):
        data = JSONParser().parse(request)
        serializer = CatagorySerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data,status =status.HTTP_201_CREATED)
        else:
            serializer = CatagorySerializer()
            return Response(serializer.errors,status =status.HTTP_400_BAD_REQUEST)   

class CatagoryDetail(APIView):
    def get_object(self,pk):
        try:
            return CatagoryModel.objects.filter(pk)
        except:
            raise Http404

    def get(self,request,pk,format=None):
        data = self.get_object(pk)
        serializer = CatagorySerializer(data)
        return Response(serializer.data)

    def delete(self,request,pk,format=None):
        data = self.get_object(pk)
        data.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
