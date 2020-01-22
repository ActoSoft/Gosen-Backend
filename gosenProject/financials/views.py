from django.shortcuts import render
from .models import Financial, Transaction
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
