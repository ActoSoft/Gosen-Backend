from rest_framework import serializers
from .models import Employee
from accounts.serializers import UserSerializerRead, UserSerializerWrite
from django.contrib.auth.models import User

class EmployeeSerializerRead(serializers.ModelSerializer):
    user = UserSerializerRead(many=False, required=True)

    class Meta:
        model = Employee
        fields = '__all__'

class EmployeeSerializerWrite(serializers.ModelSerializer):
    user = UserSerializerWrite(many=False, required=True)

    class Meta:
        model = Employee
        fields = '__all__'

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        profile = Employee.objects.create(user=user, **validated_data)
        return profile

    def update(self, instance, validated_data):
        if validated_data.get('user'):
            user_data = validated_data.pop('user')
            user = instance.user

            user.first_name = user_data.get('first_name', user.first_name)
            user.last_name = user_data.get('last_name', user.last_name)
            user.email = user_data.get('email', user.email)
            user.username = user_data.get('username', user.username)
            user.is_staff = user_data.get('is_staff', user.is_staff)
            user.save()

        instance.street = validated_data.get('street', instance.street)
        instance.city = validated_data.get('city', instance.city)
        instance.state = validated_data.get('state', instance.state)
        instance.country = validated_data.get('country', instance.country)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.role = validated_data.get('role', instance.role)
        instance.save()

        return instance
