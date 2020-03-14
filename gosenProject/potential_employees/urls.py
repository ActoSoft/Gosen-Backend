from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import PotentialEmployeeViewSet, UpdateImage

router = DefaultRouter()

router.register('', PotentialEmployeeViewSet)

urlpatterns = [
    path('update_image/', UpdateImage.as_view())
]

urlpatterns += router.urls
