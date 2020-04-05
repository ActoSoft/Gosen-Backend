from rest_framework import serializers
from ..models import Stock
from products.serializers.nested import BasicProductSerializer
from products.models import ProductStock


class StockProductSerializer(serializers.ModelSerializer):
    product = BasicProductSerializer(many=False, required=True)

    class Meta:
        model = ProductStock
        fields = ['id', 'product', 'qty']


class StockListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ['id', 'name', 'address', 'description']


class StockDetailSerializer(serializers.ModelSerializer):
    products = StockProductSerializer(many=True, required=True)

    class Meta:
        model = Stock
        fields = '__all__'
