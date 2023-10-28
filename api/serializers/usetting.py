from rest_framework.serializers import ModelSerializer
from backend.usetting.models import UserSetting

class UserSettingSerializer(ModelSerializer):
    class Meta:
        model = UserSetting
        fields = [
            'id', 
            'user', 
            'receive_notifications', 
            'discreet_notifications', 
            # 'preferred_language', 
            'time_zone', 
            'ui_mode', 
            'email_frequency',
            'created_at', 
            'updated_at',
            'is_active'
        ]
        read_only_fields = ['created_at', 'updated_at']
