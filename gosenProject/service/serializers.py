from rest_framework import serializers
from .models import Service
from works.pre_serializers import WorkSerializerOnlyRead


class ServiceSerializer(serializers.ModelSerializer):
    works = WorkSerializerOnlyRead(required=False, many=True)
    class Meta:
        model = Service
        fields = '__all__'
