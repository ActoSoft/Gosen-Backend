from rest_framework import serializers
from ..models import Product
from .common import ProductImageSerializer, ProductStockSerializer


class BasicProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'images']


class BasicProductWithStocksSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, required=False)
    stocks = ProductStockSerializer(many=True, required=False)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'images', 'stocks']
