from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
import datetime
from rest_framework.response import Response
from django.http import JsonResponse


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.filter(deleted__isnull=True)
    serializer_class = StockSerializer

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            stock = self.get_object()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        stock.deleted = now
        stock.save()
        return JsonResponse({'message': 'ok'})
