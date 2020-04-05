from django.contrib import admin
from .models import Product, ProductImage, ProductStock

admin.site.register([ProductImage, Product, ProductStock])
# Register your models here.
