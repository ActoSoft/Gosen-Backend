from rest_framework import serializers
from ..models import Work, WorkEmployee
from client.serializers.nested import BasicClientSerializer
from employee.serializers.nested import BasicEmployeeSerializer


class BasicWorkSerializer(serializers.ModelSerializer):  # Basic Work Serializer (without any nested relationship)
    class Meta:
        model = Work
        fields = '__all__'


class WorkSerializerWithClient(serializers.ModelSerializer):
    client = BasicClientSerializer(many=False, required=True)

    class Meta:
        model = Work
        fields = '__all__'


class WorkEmployeeSerializer(serializers.ModelSerializer):
    employee = BasicEmployeeSerializer(many=False, required=True)

    class Meta:
        model = WorkEmployee
        fields = '__all__'
