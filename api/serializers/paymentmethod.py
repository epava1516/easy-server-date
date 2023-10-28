from rest_framework.serializers import ModelSerializer
from backend.paymentmethod.models import PaymentMethod

class PaymentMethodSerializer(ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = ['id', 'user', 'external_id', 'type', 'last4', 'brand', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']
