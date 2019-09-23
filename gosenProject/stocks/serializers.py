from rest_framework import serializers
from .models import Stock
from products.serializers import ProductOnlyReadSerializer


class StockSerializer(serializers.ModelSerializer):
    #products = ProductOnlyReadSerializer(many=True)
    class Meta:
        model = Stock
        fields = '__all__'