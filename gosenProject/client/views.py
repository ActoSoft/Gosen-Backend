from rest_framework import viewsets, status, views
from .models import Client
from rest_framework.response import Response
from .serializers import ClientSerializerRead, ClientSerializerWrite
import datetime
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(deleted__isnull=True)
    # permission_classes = (IsAuthenticated, )
    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ClientSerializerRead
        return ClientSerializerWrite

    def destroy(self, request, pk=None):
        try:
            client = self.get_object()
        except Exception as e:
            raise e
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        client.deleted = now
        client.save()
        return JsonResponse({'message': 'ok'})

class UpdateImage(views.APIView):
    def post(self, request):
        client = Client.objects.get(id=request.data['id'])
        if request.data.get('photo'):
            client.photo = request.data['photo']
            client.save()
            clientSerialized = ClientSerializerRead(client)
            return Response(clientSerialized.data)
        else:
            return JsonResponse({'message': 'Imagen inválida'})