from django.db import models
from accounts.models import Profile

class Employee(Profile):

    def __str__(self):
        return self.user.first_name