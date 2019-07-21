from rest_framework.routers import DefaultRouter
from .views import AdminViewSet
from django.conf.urls import url

router = DefaultRouter()

router.register('', AdminViewSet)

urlpatterns = router.urls
