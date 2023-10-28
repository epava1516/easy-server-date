from rest_framework.serializers import ModelSerializer
from backend.advertisement.models import Advertisement

class AdvertisementSerializer(ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ['id', 'name', 'content', 'image', 'start_date', 'end_date', 'target_location', 'target_user_type', 'clicks', 'impressions', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['clicks', 'impressions', 'created_at', 'updated_at']
