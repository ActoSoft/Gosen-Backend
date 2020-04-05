from django.shortcuts import render
from .models import Financial, Transaction
from works.models import Work
from works.serializers.common import WorkDetailSerializer
from .serializers.common import FinancialSerializer, TransactionListSerializer, TransactionDetailSerializer
import datetime
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.filter(deleted__isnull=True)
    # permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return TransactionDetailSerializer
        else:
            return TransactionListSerializer

    def destroy(self, request, *args, **kwargs):
        try:
            transaction = self.get_object()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        transaction.deleted = now
        transaction.save()
        return Response({'message': 'ok'})


class AddTransactionRelatedToWork(views.APIView):
    def post(self, request):
        try:
            work = Work.objects.get(id=request.data['work'])
            if request.data.get('amount') and request.data.get('concept'):
                new_transaction = Transaction.objects.create(
                    amount=request.data['amount'],
                    concept=request.data['concept'],
                    type=request.data['type'],
                    work=work
                )
                if new_transaction is not None:
                    work.payed += request.data['amount']
                    work.to_pay = work.total - work.payed
                    work.save()
                    work_serialized = WorkDetailSerializer(work)
                    return Response(work_serialized.data)
                else:
                    return Response({'message': 'Algo falló al crear el pago'},
                                    status=status.HTTP_400_BAD_REQUEST)
            else:
                return Response({'message': 'Los datos enviados son inváldiso'},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({'message': 'Algo falló al crear el pago'},
                            status=status.HTTP_400_BAD_REQUEST)