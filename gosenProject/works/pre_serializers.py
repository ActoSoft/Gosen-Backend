from rest_framework import serializers
from .models import Work

class WorkSerializerOnlyRead(serializers.ModelSerializer):
    class Meta:
        model = Work
        fields = '__all__'