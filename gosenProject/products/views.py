from .models import Product, ProductImage, ProductStock
from stocks.models import Stock
from .serializers.common import ProductListSerializer, ProductDetailSerializer, ProductCreateSerializer
import datetime
from rest_framework import viewsets, status, parsers, views
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.filter(deleted__isnull=True)
    # parser_classes = [parsers.MultiPartParser]
    # permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ProductDetailSerializer
        elif self.action == 'create' or self.action == 'update':
            return ProductCreateSerializer
        else:
            return ProductListSerializer

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


class UploadImage(views.APIView):
    def post(self, request):
        try:
            print(request.data)
            product = Product.objects.get(id=request.data['id'])
            if request.data.get('image'):
                product_image = ProductImage.objects.create(
                    product=product,
                    image=request.data['image']
                )
                if product_image is not None:
                    product_serialized = ProductListSerializer(product)
                    return Response(product_serialized.data)
                else:
                    return JsonResponse({'message': 'Algo falló al guardar'})
            else:
                return JsonResponse({'message': 'Imagen inválida'})
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteImage(views.APIView):
    def post(self, request):
        try:
            product_image = ProductImage.objects.get(id=request.data['id'])
            product = Product.objects.get(id=product_image.product.id)
            product_image.delete()
            product_serialized = ProductListSerializer(product)
            return Response(product_serialized.data)
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)


class SaveStock(views.APIView):
    def post(self, request):
        try:
            if not request.data.get('stock'):
                return Response({"message": "Not stock in request"}, status=status.HTTP_400_BAD_REQUEST)
            elif not request.data.get('product'):
                return Response({"message": "Not product in request"}, status=status.HTTP_400_BAD_REQUEST)
            elif not request.data.get('qty') or request.data['qty'] < 1:
                return Response({"message": "Not qty in request"}, status=status.HTTP_400_BAD_REQUEST)
            stock = Stock.objects.get(id=request.data['stock'])
            product = Product.objects.get(id=request.data['product'])
            product_stock = ProductStock.objects.create(
                product=product,
                stock=stock,
                qty=request.data['qty']
            )
            if product_stock is not None:
                product_serializer = ProductDetailSerializer(product)
                return Response(product_serializer.data)
            else:
                return Response({"message": "Algo falló al guardar"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": "Algo falló al guardar"}, status=status.HTTP_400_BAD_REQUEST)
