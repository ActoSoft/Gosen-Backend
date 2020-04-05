from rest_framework import viewsets, status, views
from .models import Employee
from rest_framework.response import Response
from .serializers.common import EmployeeDetailSerializer, EmployeeSerializerWrite, EmployeeListSerializer
import datetime
from django.http import JsonResponse


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.filter(deleted__isnull=True)
    # permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            if self.action == 'retrieve':
                return EmployeeDetailSerializer
            return EmployeeListSerializer
        return EmployeeSerializerWrite

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            employee = self.get_object()
        except Exception as e:
            print(e)
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
            employee_serialized = EmployeeDetailSerializer(employee)
            return Response(employee_serialized.data)
        else:
            return JsonResponse({'message': 'Imagen inválida'})
