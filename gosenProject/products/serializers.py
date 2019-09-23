from rest_framework import serializers
from .models import Product, ProductImage
from stocks.serializers import StockSerializer


class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = '__all__'


class ProductOnlyReadSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['name', 'description', 'barcode', 'qty', 'images']


class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    stocks = StockSerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'