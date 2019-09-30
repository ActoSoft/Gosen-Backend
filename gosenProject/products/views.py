from django.shortcuts import render
from .models import Product, ProductImage
from .serializers import ProductSerializer
import datetime
from rest_framework import viewsets, status, response, parsers
from rest_framework.response import Response


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(deleted__isnull=True)
    serializer_class = ProductSerializer
    parser_classes = [parsers.MultiPartParser]

    def create(self, request):
        if not request.data.get('barcode'):
            barcode = None
        product = Product.objects.create(
            barcode=barcode,
            name=request.data['name'],
            description=request.data['description']
        )

        if request.data.get('image'):
            ProductImage.objects.create(
                product=product,
                image=request.data['image']
            )
        return Response(ProductSerializer(product).data)