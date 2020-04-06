from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from .models import Service
from .serializers.common import ServiceSerializer, ServiceListSerializer
import datetime
from rest_framework.response import Response
from django.http import JsonResponse


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(deleted__isnull=True)
    serializer_class = ServiceSerializer
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == "list":
            return ServiceListSerializer
        return ServiceSerializer

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            service = self.get_object()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        service.deleted = now
        service.save()
        return JsonResponse({'message': 'ok'})
