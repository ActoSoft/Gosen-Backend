from rest_framework.routers import DefaultRouter
from .views import ClientViewSet
from django.conf.urls import url

router = DefaultRouter()

router.register('', ClientViewSet)

urlpatterns = router.urls