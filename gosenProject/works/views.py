from rest_framework import viewsets, views, status
from rest_framework.response import Response
from .models import Work, WorkEmployee
from client.models import Client
from service.models import Service
from employee.models import Employee
from financials.models import Transaction
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
                transaction = Transaction.objects.create(
                    amount=data['payed'],
                    concept='Anticipo',
                    type='income',
                    work=work
                )

                if transaction is not None:
                    work_with_employees = Work.objects.get(id=work.id)
                    work_serializer = WorkDetailSerializer(work_with_employees)
                    return Response(work_serializer.data)
                else:
                    return Response({'message': 'Algo falló al crear el trabajo'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Algo falló al crear el trabajo'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class UpdateWork(views.APIView):
    def post(self, request):
        try:
            data = request.data
            if not data.get('id') or data['id'] is None:
                return Response({'message': 'Trabajo no existente o inválido'}, status=status.HTTP_400_BAD_REQUEST)
            if not data.get('clientId') or data['clientId'] is None:
                return Response({'message': 'Cliente no existente o inválido'}, status=status.HTTP_400_BAD_REQUEST)
            if not data.get('serviceId') or data['serviceId'] is None:
                return Response({'message': 'Servicio no existente o inválido'}, status=status.HTTP_400_BAD_REQUEST)
            if not data.get('employeesId') or data['employeesId'] is None or len(data['employeesId']) < 1:
                return Response({'message': 'Empleados nos existentes o inválidos'}, status=status.HTTP_400_BAD_REQUEST)
            client = Client.objects.get(id=data['clientId'])
            service = Service.objects.get(id=data['serviceId'])
            work = Work.objects.get(id=data['id'])
            work.client = client
            work.service = service
            work.datetime_start = data['dateStart']
            work.datetime_end = data['dateEnd']
            work.status = data['status']
            work.qty = data['qty']
            work.total = data['total']
            work.to_pay = data['toPay']
            work.description = data['description']
            work.save()

            if data.get('newEmployees'):
                for new_employee in data['newEmployees']:
                    employee = Employee.objects.get(id=new_employee)
                    WorkEmployee.objects.create(
                        employee=employee,
                        work=work
                    )

            if data.get('removedEmployees'):
                for removed_employee in data['removedEmployees']:
                    print(removed_employee)
                    print(work.id)
                    work_employee_to_delete = WorkEmployee.objects.filter(employee__id=removed_employee, work=work)
                    print(work_employee_to_delete)
                    work_employee_to_delete.delete()
            work_serializer = WorkDetailSerializer(Work.objects.get(id=work.id))
            return Response(work_serializer.data)

        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)