from rest_framework import viewsets, status
from .models import Service
from .serializers import ServiceSerializer
import datetime
from rest_framework.response import Response
from django.http import JsonResponse


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.filter(deleted__isnull=True)
    serializer_class = ServiceSerializer

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            service = self.get_object()
        except Exception as e:
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        service.deleted = now
        service.save()
        return JsonResponse({'message': 'ok'})
