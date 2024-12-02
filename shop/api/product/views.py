from django.shortcuts import render
from rest_framework import viewsets
from .models import Product
from .serializers import ProductSerializers

# Create your views here.

class ProductView(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializers