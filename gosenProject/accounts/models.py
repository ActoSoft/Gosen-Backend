from django.db import models
from django.contrib.auth.models import User

GENDERS_LIST = (
    ('masculino', 'Masculino'),
    ('femenino', 'Femenino'),
    ('otro', 'Otro')
)

class Profile (models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street = models.CharField(max_length=150, blank=True, null=True)
    city = models.CharField(max_length=150, blank=True, null=True)
    state = models.CharField(max_length=150, blank=True, null=True)
    country = models.CharField(max_length=150, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    gender = models.CharField(choices=GENDERS_LIST, max_length=50)
    photo = models.ImageField(upload_to="image/%Y/%m/%d", default="default.png")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)
