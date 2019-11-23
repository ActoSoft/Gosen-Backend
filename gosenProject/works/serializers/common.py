from rest_framework import serializers
from ..models import Work, WorkEmployee
from client.serializers.nested import BasicClientSerializer
from service.serializers.nested import BasicServiceSerializer
from .nested import WorkEmployeeSerializer


class WorkSerializer(serializers.ModelSerializer):
    client = BasicClientSerializer(many=False, required=True)
    service = BasicServiceSerializer(many=False, required=True)
    employees = WorkEmployeeSerializer(many=True, required=False)

    class Meta:
        model = Work
        fields = '__all__'


