from django.contrib import admin
from .models import Financial, Transaction

admin.site.register([Financial, Transaction])
