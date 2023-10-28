from rest_framework.serializers import ModelSerializer
from backend.notification.models import Notification

class NotificationSerializer(ModelSerializer):
    class Meta:
        model = Notification
        fields = ['id', 'user', 'content', 'is_read', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']
