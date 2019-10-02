from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import AdminViewSet, UpdateImage
from django.conf.urls import url

router = DefaultRouter()

router.register('', AdminViewSet)

urlpatterns = [
    path('update_image/', UpdateImage.as_view())
]

urlpatterns += router.urls

