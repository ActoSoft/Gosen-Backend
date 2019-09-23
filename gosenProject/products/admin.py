from django.contrib import admin
from .models import Product, ProductImage

admin.site.register([ProductImage, Product])
# Register your models here.
