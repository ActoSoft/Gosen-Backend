from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TransactionViewSet, AddTransactionRelatedToWork

router = DefaultRouter()
router.register('transactions', TransactionViewSet)

urlpatterns = [
    path('create_transaction/', AddTransactionRelatedToWork.as_view())
]

urlpatterns += router.urls