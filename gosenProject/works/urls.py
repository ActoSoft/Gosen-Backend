from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import WorkViewSet, CreateWork, UpdateWork

router = DefaultRouter()
router.register('', WorkViewSet)

urlpatterns = [
    path('create_work/', CreateWork.as_view()),
    path('update_work/', UpdateWork.as_view())

]
urlpatterns += router.urls
