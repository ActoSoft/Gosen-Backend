from django.db import models
from accounts.models import Profile
from django.contrib.auth.models import User

PAYMENT_TIPE_LIST = (
    ('semanal', 'Semanal'),
    ('quincenal', 'Quincenal'),
    ('mensual', 'Mensual'),
)


class Employee(Profile):
    contract_date_start = models.DateTimeField(blank=True, null=True)
    contracted_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='contractor', blank=True, null=True)
    vigency = models.CharField(max_length=150, blank=True, null=True)
    salary = models.CharField(max_length=150, blank=True, null=True)
    payment_type = models.CharField(choices=PAYMENT_TIPE_LIST, max_length=100, default='Quincenal')
    active = models.BooleanField(default=True)
    fired = models.BooleanField(default=False)
    fired_date = models.DateTimeField(blank=True, null=True)
    fired_by = models.OneToOneField(User, on_delete=models.CASCADE, related_name='firer', blank=True, null=True)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.first_name
