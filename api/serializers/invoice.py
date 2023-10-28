from rest_framework.serializers import ModelSerializer
from backend.invoice.models import Invoice

class InvoiceSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['id', 'transaction', 'issued_date', 'due_date', 'is_paid', 'invoice_pdf', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['issued_date', 'created_at', 'updated_at']
