from django.shortcuts import render
from rest_framework import viewsets
from .models import Admin
from .serializers import AdminSerializerRead, AdminSerializerWrite

class AdminViewSet(viewsets.ModelViewSet):
    #serializer_class = AdminSerializer
    queryset = Admin.objects.all()

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return AdminSerializerRead
        return AdminSerializerWrite
