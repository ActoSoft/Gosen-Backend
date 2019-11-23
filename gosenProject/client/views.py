from rest_framework import viewsets, status, views
from .models import Client
from rest_framework.response import Response
from .serializers.common import ClientSerializerRead, ClientSerializerWrite
import datetime
from django.http import JsonResponse


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.filter(deleted__isnull=True)
    # permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ClientSerializerRead
        return ClientSerializerWrite

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            client = self.get_object()
        except Exception as e:
            print(e)
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
            client_serialized = ClientSerializerRead(client)
            return Response(client_serialized.data)
        else:
            return JsonResponse({'message': 'Imagen inválida'})
