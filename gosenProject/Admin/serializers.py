from rest_framework import serializers
from .models import Admin
from accounts.serializers import UserSerializerRead, UserSerializerWrite
from django.contrib.auth.models import User

class AdminSerializerRead(serializers.ModelSerializer):
    user = UserSerializerRead(many=False, required=True)

    class Meta:
        model = Admin
        fields = '__all__'

class AdminSerializerWrite(serializers.ModelSerializer):
    user = UserSerializerWrite(many=False, required=True)

    class Meta:
        model = Admin
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data, is_staff=True)
        user.set_password(user_data['password'])
        user.save()
        profile = Admin.objects.create(user=user, **validated_data)
        return profile
