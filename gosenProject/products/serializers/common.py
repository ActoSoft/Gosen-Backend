from rest_framework import serializers
from ..models import Product, ProductStock, ProductImage
from stocks.serializers.nested import BasicStockSerializer


class ProductImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ProductImage
        fields = ['id', 'image']


class ProductStockSerializer(serializers.ModelSerializer):
    stock = BasicStockSerializer(many=False, required=True)

    class Meta:
        model = ProductStock
        fields = ['stock', 'qty']


class ProductListSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'images']


class ProductDetailSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    stocks = ProductStockSerializer(many=True, required=True)

    class Meta:
        model = Product
        fields = '__all__'
