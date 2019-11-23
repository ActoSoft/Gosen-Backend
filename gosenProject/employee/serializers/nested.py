from rest_framework import serializers
from ..models import Employee
from accounts.serializers.nested import BasicUserSerializerRead


class BasicEmployeeSerializer(serializers.ModelSerializer):
    user = BasicUserSerializerRead(many=False, required=True)

    class Meta:
        model = Employee
        fields = '__all__'

