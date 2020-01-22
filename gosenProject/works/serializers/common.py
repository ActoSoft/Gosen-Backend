from rest_framework import serializers
from ..models import Work
from client.serializers.nested import BasicClientSerializer
from service.serializers.nested import BasicServiceSerializer
from financials.serializers.nested import TransactionSerializer
from .nested import WorkEmployeeSerializer


class WorkListSerializer(serializers.ModelSerializer):
    client = BasicClientSerializer(many=False, required=True)
    service = BasicServiceSerializer(many=False, required=True)
    employees = WorkEmployeeSerializer(many=True, required=False)

    class Meta:
        model = Work
        fields = '__all__'


class WorkDetailSerializer(serializers.ModelSerializer):
    client = BasicClientSerializer(many=False, required=True)
    service = BasicServiceSerializer(many=False, required=True)
    employees = WorkEmployeeSerializer(many=True, required=False)
    transactions = TransactionSerializer(many=True, required=True)

    class Meta:
        model = Work
        fields = '__all__'
