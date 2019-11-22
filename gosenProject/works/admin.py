from django.contrib import admin
from .models import Work, WorkEmployee
# Register your models here.
admin.site.register([Work, WorkEmployee])