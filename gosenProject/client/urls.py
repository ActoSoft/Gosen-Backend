from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ClientViewSet, UpdateImage

router = DefaultRouter()

router.register('', ClientViewSet)

urlpatterns = [
    path('update_image/', UpdateImage.as_view())
]

urlpatterns += router.urls
