from django.shortcuts import render
from rest_framework import viewsets, status
from .models import Client
from rest_framework.response import Response
from .serializers import ClientSerializerRead, ClientSerializerWrite
import datetime
from django.http import JsonResponse

class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(deleted__isnull=True)

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ClientSerializerRead
        return ClientSerializerWrite

    def destroy(self, request, pk=None):
        try:
            client = self.get_object()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        client.deleted = now
        client.save()
        return JsonResponse({'message': 'ok'})