from rest_framework import serializers
from .models import Product, ProductImage, ProductStock


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductOnlyReadSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'barcode', 'images']


class ProductStockSerializer(serializers.ModelSerializer):
    product = ProductOnlyReadSerializer(many=False, required=True)

    class Meta:
        model = ProductStock
        fields = ['product', 'qty']