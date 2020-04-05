from rest_framework import serializers
from ..models import Service
from works.serializers.nested import WorkSerializerWithClient


class ServiceListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Service
        fields = ['id', 'name', 'cost', 'description']


class ServiceSerializer(serializers.ModelSerializer):
    works = WorkSerializerWithClient(many=True, required=False)

    class Meta:
        model = Service
        fields = '__all__'
