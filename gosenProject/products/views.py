from .models import Product, ProductImage
from .serializers.common import ProductListSerializer, ProductDetailSerializer
import datetime
from rest_framework import viewsets, status, parsers
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(deleted__isnull=True)
    parser_classes = [parsers.MultiPartParser]
    # permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        else:
            return ProductListSerializer

    # def create(self, request):
    #     if not request.data.get('barcode'):
    #         barcode = None
    #     product = Product.objects.create(
    #         barcode=barcode,
    #         name=request.data['name'],
    #         description=request.data['description']
    #     )
    #
    #     if request.data.get('image'):
    #         ProductImage.objects.create(
    #             product=product,
    #             image=request.data['image']
    #         )
    #     return Response(ProductSerializer(product).data)

    def destroy(self, request, *args, **kwargs):
        try:
            product = self.get_object()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        product.deleted = now
        product.save()
        return JsonResponse({'message': 'ok'})
