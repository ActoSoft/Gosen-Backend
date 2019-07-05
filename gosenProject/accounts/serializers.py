from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Profile

class UserSerializerRead(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_staff')

class UserSerializerWrite(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password', 'is_staff')
