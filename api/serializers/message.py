from rest_framework.serializers import ModelSerializer
from backend.message.models import Message

class MessageSerializer(ModelSerializer):
    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'content', 'is_read', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']