from rest_framework import serializers
from .models import Stock
from products.preserializers import ProductStockSerializer


class StockSerializer(serializers.ModelSerializer):
    products = ProductStockSerializer(many=True, required=False)

    class Meta:
        model = Stock
        fields = '__all__'