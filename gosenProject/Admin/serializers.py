from rest_framework import serializers
from .models import Admin
from accounts.serializers import UserSerializer

class AdminSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False, required=True)
    class Meta:
        model = Admin
        fields = '__all__'