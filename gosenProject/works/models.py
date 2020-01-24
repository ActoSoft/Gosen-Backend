from django.db import models
from service.models import Service
from client.models import Client
from employee.models import Employee
# Create your models here.


class Work(models.Model):
    STATUS_CHOICES = [
        ('in_progress', 'En Curso'),
        ('finished', 'Finalizado'),
        ('pending', 'Pendiente'),
        ('authorized', 'Autorizado'),
        ('canceled', 'Cancelado')
    ]
    qty = models.PositiveIntegerField(default=0)
    total = models.DecimalField(max_digits=8, decimal_places=2)
    payed = models.DecimalField(max_digits=8, decimal_places=2)
    to_pay = models.DecimalField(max_digits=8, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="pending")
    description = models.TextField(blank=True, null=True)
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    service = models.ForeignKey(Service, related_name='works', on_delete=models.CASCADE)
    client = models.ForeignKey(Client, related_name='works', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.service.name + " " + self.client.user.username


class WorkEmployee(models.Model):
    employee = models.ForeignKey(Employee, related_name="works", on_delete=models.CASCADE)
    work = models.ForeignKey(Work, related_name="employees", on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    deleted = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.employee.user.username + " - " + self.work.status


