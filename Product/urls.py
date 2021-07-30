from django.contrib import admin
from django.urls import path,include
from Product import views
from Product.views import *


urlpatterns = [
    path('',views.Product.as_view(), name='product'),
    path('detail/<int:pk>/',views.Product.as_view(), name='product_detail'),

    path('catagory/',views.Catagory.as_view(), name='catagory'),
    path('catagory/detail/<int:pk>/',views.CatagoryDetail.as_view(), name='catagory_detail'),
]
