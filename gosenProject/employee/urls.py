from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from django.conf.urls import url

router = DefaultRouter()

router.register('', EmployeeViewSet)

urlpatterns = router.urls