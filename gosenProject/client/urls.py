from rest_framework.routers import DefaultRouter
from .views import ClientViewSet

router = DefaultRouter()

router.register('', ClientViewSet)

urlpatterns = router.urls
