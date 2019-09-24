from django.db import models
from stocks.models import Stock


class Product(models.Model):
    barcode = models.CharField(max_length=50, blank=True, null=True)
    name = models.CharField(max_length=140)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name


class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='products', blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.product.name


class ProductStock(models.Model):
    product = models.ForeignKey(Product, related_name='stocks', on_delete=models.CASCADE)
    stock = models.ForeignKey(Stock, related_name='products', on_delete=models.CASCADE)
    qty = models.PositiveIntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'{self.product.name} - Stock: {self.stock.name}'