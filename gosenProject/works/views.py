from rest_framework import viewsets
from .models import Work
from .serializers.common import WorkSerializer


class WorkViewSet(viewsets.ModelViewSet):
    queryset = Work.objects.filter(deleted__isnull=True)
    serializer_class = WorkSerializer
