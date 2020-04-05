from django.db import models
from works.models import Work

CHOICES = (
    ('income', 'Ingreso'),
    ('egress', 'Egreso')
)


class Financial(models.Model):

    total_income = models.DecimalField(decimal_places=2, max_digits=9)
    total_egress = models.DecimalField(decimal_places=2, max_digits=9)
    total = models.DecimalField(decimal_places=2, max_digits=9)
    utility = models.DecimalField(decimal_places=2, max_digits=4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.id


class Transaction(models.Model):
    amount = models.DecimalField(decimal_places=2, max_digits=9)
    concept = models.TextField()
    type = models.CharField(max_length=20, choices=CHOICES)
    work = models.ForeignKey(Work, related_name='transactions', blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f'Work #{self.work.id} - {self.concept}'
