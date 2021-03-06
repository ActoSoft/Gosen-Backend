from rest_framework import viewsets, status, views
from rest_framework.permissions import IsAuthenticated
from .models import Admin
from rest_framework.response import Response
from Admin.serializers.common import AdminListSerializer, AdminDetailSerializer, AdminSerializerWrite
import datetime
from django.http import JsonResponse


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.filter(deleted__isnull=True)
    permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            if self.action == "retrieve":
                return AdminDetailSerializer
            return AdminListSerializer
        return AdminSerializerWrite

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            admin = self.get_object()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        admin.deleted = now
        admin.save()
        return JsonResponse({'message': 'ok'})


class UpdateImage(views.APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        admin = Admin.objects.get(id=request.data['id'])
        if request.data.get('photo'):
            admin.photo = request.data['photo']
            admin.save()
            admin_serialized = AdminDetailSerializer(admin)
            return Response(admin_serialized.data)
        else:
            return JsonResponse({'message': 'Imagen inválida'})
