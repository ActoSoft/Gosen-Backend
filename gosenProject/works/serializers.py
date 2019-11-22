from rest_framework import serializers
from .models import Work, WorkEmployee
from service.serializers import ServiceSerializer
from client.serializers import ClientSerializerRead
from employee.serializers import EmployeeSerializerRead

class WorkSerializerOnlyRead(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'

class WorkEmployeeSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializerRead(many=False, required=False)
    class Meta:
        model = WorkEmployee
        fields = '__all__'

class WorkSerializer(serializers.ModelSerializer):
    service = ServiceSerializer(many=False, required=True)
    client = ClientSerializerRead(many=False, required=True)
    employees = WorkEmployeeSerializer(many=True)
    class Meta:
        model = Work
        fields = '__all__'
