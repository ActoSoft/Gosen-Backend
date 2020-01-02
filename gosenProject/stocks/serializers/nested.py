from rest_framework import serializers
from ..models import Stock


class BasicStockSerializer(serializers.ModelSerializer):

    class Meta:
        model = Stock
        fields = ['id', 'name', 'address', 'description', 'deleted']


