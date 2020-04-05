from rest_framework.serializers import ModelSerializer
from ..models import Financial, Transaction
from works.serializers.nested import WorkSerializerWithClient


class FinancialSerializer(ModelSerializer):
    class Meta:
        model = Financial
        fields = '__all__'


class TransactionListSerializer(ModelSerializer):
    work = WorkSerializerWithClient

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'concept', 'type', 'work']


class TransactionDetailSerializer(ModelSerializer):
    work = WorkSerializerWithClient

    class Meta:
        model = Transaction
        fields = '__all__'
