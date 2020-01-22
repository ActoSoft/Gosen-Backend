from rest_framework import viewsets
from .models import Work
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
