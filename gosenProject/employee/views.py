from rest_framework import viewsets, status, views
from .models import Employee
from rest_framework.response import Response
from .serializers import EmployeeSerializerRead, EmployeeSerializerWrite
import datetime
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(deleted__isnull=True)
    # permission_classes = (IsAuthenticated, )
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

class UpdateImage(views.APIView):
    def post(self, request):
        employee = Employee.objects.get(id=request.data['id'])
        if request.data.get('photo'):
            employee.photo = request.data['photo']
            employee.save()
            employeeSerialized = EmployeeSerializerRead(employee)
            return Response(employeeSerialized.data)
        else:
            return JsonResponse({'message': 'Imagen inválida'})
