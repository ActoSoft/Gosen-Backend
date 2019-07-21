from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Admin
from rest_framework.response import Response
from .serializers import AdminSerializerRead, AdminSerializerWrite
import datetime
from django.http import JsonResponse


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.filter(deleted__isnull=True)

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return AdminSerializerRead
        return AdminSerializerWrite

    def destroy(self, request, pk=None):
        try:
            admin = self.get_object()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        admin.deleted = now
        admin.save()
        return JsonResponse({'message': 'ok'})
