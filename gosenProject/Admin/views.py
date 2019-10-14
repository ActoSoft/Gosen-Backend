from django.shortcuts import render
from rest_framework import viewsets, status, views
from .models import Admin
from rest_framework.response import Response
from .serializers import AdminSerializerRead, AdminSerializerWrite
import datetime
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.filter(deleted__isnull=True)
    permission_classes = (IsAuthenticated, )
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return AdminSerializerRead
        return AdminSerializerWrite

    def destroy(self, request, pk=None):
        try:
            admin = self.get_object()
        except Exception as e:
            raise e
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        admin.deleted = now
        admin.save()
        return JsonResponse({'message': 'ok'})


class UpdateImage(views.APIView):
    def post(self, request):
        admin = Admin.objects.get(id=request.data['id'])
        print(admin)
        if request.data.get('photo'):
            admin.photo = request.data['photo']
            admin.save()
            adminSerialized = AdminSerializerRead(admin)
            return Response(adminSerialized.data)
        else:
            return JsonResponse({'message': 'Imagen inválida'})