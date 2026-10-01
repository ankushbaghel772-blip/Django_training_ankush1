from django.urls import path

from .views import *

urlpatterns = [

    path('deleteproduct/', deleteproduct, name='deleteproduct'),

    path('updateproduct/', updateproduct, name='updateproduct'),

    path('productlist/', productlist, name='productlist'),

    path('saveproduct/', saveproduct, name='saveproduct'),

    path('newProductForm/', newProductForm, name='newProductForm'),

    path('updateproductform/', updateproductform, name='updateproductform'),

]