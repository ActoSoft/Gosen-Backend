from django.db import models


class Stock(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    address = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
