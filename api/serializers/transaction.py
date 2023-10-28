from rest_framework.serializers import ModelSerializer
from backend.transaction.models import Transaction

class TransactionSerializer(ModelSerializer):
    class Meta:
        model = Transaction
        fields = [
            'id', 
            'user', 
            'transaction_type', 
            'amount', 
            'currency', 
            'status', 
            'payment_method', 
            'external_id', 
            'is_successful', 
            'payment_gateway_response', 
            'is_active', 
            'created_at', 
            'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']