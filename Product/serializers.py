from rest_framework import serializers
from Product.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = '__all__'
class CatagorySerializer(serializers.ModelSerializer):
    class Meta:
        model = CatagoryModel
        fields = '__all__'