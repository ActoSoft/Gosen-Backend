from django.db import models

PAYMENT_TIPE_LIST = (
    ('semanal', 'Semanal'),
    ('quincenal', 'Quincenal'),
    ('mensual', 'Mensual'),
)

class Service(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    description = models.CharField(max_length=150, blank=True, null=True)
    cost = models.CharField(max_length=150, blank=True, null=True)
    payment_tipe = models.CharField(choices=PAYMENT_TIPE_LIST, max_length=100, default='Quincenal')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name