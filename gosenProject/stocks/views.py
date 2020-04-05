from rest_framework.viewsets import ModelViewSet
from rest_framework import status, views
from .models import Stock
from products.models import Product, ProductStock
from .serializers.common import StockListSerializer, StockDetailSerializer, StockProductSerializer
import datetime
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.filter(deleted__isnull=True)
    # permission_classes = (IsAuthenticated, )

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return StockDetailSerializer
        return StockListSerializer

    def destroy(self, request, pk=None, *args, **kwargs):
        try:
            stock = self.get_object()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_404_NOT_FOUND)
        now = datetime.datetime.now()
        stock.deleted = now
        stock.save()
        return JsonResponse({'message': 'ok'})


class SaveProduct(views.APIView):
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
                stock_serializer = StockDetailSerializer(stock)
                return Response(stock_serializer.data)
            else:
                return Response({"message": "Algo falló al guardar"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": "Algo falló al guardar"}, status=status.HTTP_400_BAD_REQUEST)


class UpdateQtyInProduct(views.APIView):
    def post(self, request):
        try:
            if not request.data.get('id'):
                return Response({"message": "Not id in request"}, status=status.HTTP_400_BAD_REQUEST)
            elif not request.data.get('qty'):
                return Response({"message": "Not qty in request"}, status=status.HTTP_400_BAD_REQUEST)
            product_stock = ProductStock.objects.get(id=request.data['id'])
            if product_stock is not None:
                product_stock.qty = request.data['qty']
                product_stock.save()
                product_stock_serializer = StockProductSerializer(product_stock)
                return Response(product_stock_serializer.data)

            else:
                return Response({"message": "Algo falló al actualizar la cantidad"}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({"message": "Algo falló al actualizar la cantidad"}, status=status.HTTP_400_BAD_REQUEST)


class DeleteProduct(views.APIView):
    def post(self, request):
        try:
            if not request.data.get('id'):
                return Response({"message": "Not id in request"}, status=status.HTTP_400_BAD_REQUEST)
            product_stock = ProductStock.objects.get(id=request.data['id'])
            if product_stock is not None:
                now = datetime.datetime.now()
                product_stock.delete()
                stock = Stock.objects.get(id=product_stock.stock.id)
                stock_serialized = StockDetailSerializer(stock)
                return Response(stock_serialized.data)
            else:
                return Response({"message": "Algo falló al eliminar el producto del almacén"},
                                status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            print(e)
            return Response({"message": "Algo falló al eliminar el producto del almacén"},
                            status=status.HTTP_400_BAD_REQUEST)