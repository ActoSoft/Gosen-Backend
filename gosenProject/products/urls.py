from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, UploadImage, DeleteImage

router = DefaultRouter()

router.register('', ProductViewSet)


urlpatterns = [
    path('upload_image/', UploadImage.as_view()),
    path('delete_image/', DeleteImage.as_view())
]
urlpatterns += router.urls
