from rest_framework import viewsets, status
from .models import Work, WorkEmployee
from .serializers import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.filter(deleted__isnull=True)
    serializer_class = WorkSerializer
