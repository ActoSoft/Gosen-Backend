from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import StockViewSet, SaveProduct, UpdateQtyInProduct, DeleteProduct

router = DefaultRouter()

router.register('', StockViewSet)

urlpatterns = [
    path('save_product/', SaveProduct.as_view()),
    path('update_qty/', UpdateQtyInProduct.as_view()),
    path('delete_product/', DeleteProduct.as_view())
]

urlpatterns += router.urls
