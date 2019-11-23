from rest_framework import serializers
from ..models import Client
from accounts.serializers.nested import BasicUserSerializerRead


class BasicClientSerializer(serializers.ModelSerializer):
    user = BasicUserSerializerRead(many=False, required=True)
    
    class Meta:
        model = Client
        fields = '__all__'
