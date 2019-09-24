from rest_framework import serializers
from .models import Stock
from products.models import ProductStock


class StockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = '__all__'


class StockProductSerializer(serializers.ModelSerializer):
    stock = StockSerializer(many=False)

    class Meta:
        model = ProductStock
        fields = ['stock', 'qty']