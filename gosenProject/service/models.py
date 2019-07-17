from django.db import models

PAYMENT_TIPE_LIST = (
    ('hora', 'Hora'),
    ('dia', 'Dia'),
    ('semanal', 'Semanal'),
    ('quincenal', 'Quincenal'),
    ('mensual', 'Mensual'),
    ('bimestral', 'Bimestral'),
    ('trimestral', 'Trimestral'),
    ('semestral', 'Semestral'),
    ('anual', 'Anual')
)


class Service(models.Model):
    name = models.CharField(max_length=150, blank=False)
    description = models.CharField(max_length=150, blank=True, null=True)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    payment_type = models.CharField(choices=PAYMENT_TIPE_LIST, max_length=100, default='Quincenal')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.name
