from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .models import Work, WorkEmployee
from client.models import Client
from service.models import Service
from employee.models import Employee
from .serializers.common import WorkListSerializer, WorkDetailSerializer
from rest_framework.permissions import IsAuthenticated


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.filter(deleted__isnull=True)
    # permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return WorkDetailSerializer
        else:
            return WorkListSerializer


class CreateWork(views.APIView):
    def post(self, request):
        try:
            data = request.data
            if not data.get('clientId') or data['clientId'] is None:
                return Response({'message': 'Cliente no existente o inválido'}, status=status.HTTP_400_BAD_REQUEST)
            if not data.get('serviceId') or data['serviceId'] is None:
                return Response({'message': 'Servicio no existente o inválido'}, status=status.HTTP_400_BAD_REQUEST)
            if not data.get('employeesId') or data['employeesId'] is None or len(data['employeesId']) < 1:
                return Response({'message': 'Empleados nos existentes o inválidos'}, status=status.HTTP_400_BAD_REQUEST)
            client = Client.objects.get(id=data['clientId'])
            service = Service.objects.get(id=data['serviceId'])
            work = Work.objects.create(
                client=client,
                service=service,
                datetime_start=data['dateStart'],
                datetime_end=data['dateEnd'],
                status=data['status'],
                qty=data['qty'],
                total=data['total'],
                payed=data['payed'],
                to_pay=data['toPay'],
                description=data['description']
            )
            if work is not None:
                for employeeId in data['employeesId']:
                    employee = Employee.objects.get(id=employeeId)
                    WorkEmployee.objects.create(
                        employee=employee,
                        work=work
                    )
                work_with_employees = Work.objects.get(id=work.id)
                work_serializer = WorkDetailSerializer(work_with_employees)
                return Response(work_serializer.data)
            else:
                return Response({'message': 'Algo falló al crear el trabajo'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
