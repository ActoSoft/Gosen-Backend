from rest_framework import viewsets, status
from .models import Employee
from rest_framework.response import Response
from .serializers import EmployeeSerializerRead, EmployeeSerializerWrite
import datetime
from django.http import JsonResponse


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(deleted__isnull=True)

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return EmployeeSerializerRead
        return EmployeeSerializerWrite

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            employee = self.get_object()
        except Exception as e:
            raise e
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        employee.deleted = now
        employee.save()
        return JsonResponse({'message': 'ok'})
