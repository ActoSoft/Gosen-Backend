from django.db import models
from accounts.models import Profile


ROLE_EMPLOYEE_LIST = (
    ('sales', 'Ventas'),
    ('internal', 'Interno')
)


class PotentialEmployee(Profile):
    role = models.CharField(max_length=20, choices=ROLE_EMPLOYEE_LIST)
    observations = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.user.first_name + ' ' + self.role
