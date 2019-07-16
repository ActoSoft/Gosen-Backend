from rest_framework.routers import DefaultRouter
from .views import ServiceViewSet
from django.conf.urls import url

router = DefaultRouter()

router.register('', ServiceViewSet)

urlpatterns = router.urls