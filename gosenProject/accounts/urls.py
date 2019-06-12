from django.urls import path
from rest_framework.routers import DefaultRouter

app_name = 'accounts'

router = DefaultRouter()

router.register(r'login', MovieViewSet)
router.register(r'forgot_password', DirectorViewSet)

urlpatterns = router.urls