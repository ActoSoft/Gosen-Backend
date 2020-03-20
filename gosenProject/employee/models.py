from django.db import models
from accounts.models import Profile
from Admin.models import Admin

PAYMENT_TYPE_LIST = (
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

ROLE_LIST = (
    ('sales', 'Ventas'),
    ('internal', 'Interno')
)


class Employee(Profile):
    contract_date_start = models.DateField(blank=True, null=True)
    role = models.CharField(max_length=20, choices=ROLE_LIST)
    contracted_by = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='contractor', blank=True, null=True)
    vigency = models.CharField(max_length=150, blank=True, null=True)
    salary = models.CharField(max_length=150, blank=True, null=True)
    payment_type = models.CharField(choices=PAYMENT_TYPE_LIST, max_length=100, default='Quincenal')
    active = models.BooleanField(default=True)
    fired = models.BooleanField(default=False)
    fired_date = models.DateField(blank=True, null=True)
    fired_by = models.ForeignKey(Admin, on_delete=models.CASCADE, related_name='firer', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name
