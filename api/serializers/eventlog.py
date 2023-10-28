from rest_framework.serializers import ModelSerializer
from backend.eventlog.models import EventLog

class EventLogSerializer(ModelSerializer):
    class Meta:
        model = EventLog
        fields = ['id', 'user', 'action', 'details', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']
