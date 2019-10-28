from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, UpdateImage

router = DefaultRouter()

router.register('', EmployeeViewSet)

urlpatterns = [
    path('update_image/', UpdateImage.as_view())
]

urlpatterns += router.urls
