from rest_framework import serializers
from ..models import Admin
from accounts.serializers.nested import BasicUserSerializerRead


class BasicAdminSerializer(serializers.ModelSerializer):
    user = BasicUserSerializerRead(many=False, required=True)

    class Meta:
        model = Admin
        fields = '__all__'
