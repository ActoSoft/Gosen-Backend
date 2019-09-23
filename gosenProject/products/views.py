from django.shortcuts import render
from .models import Product, ProductImage
from .serializers import ProductSerializer
import datetime
from rest_framework import viewsets, status, response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(deleted__isnull=True)
    serializer_class = ProductSerializer
