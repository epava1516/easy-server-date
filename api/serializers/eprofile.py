from rest_framework.serializers import ModelSerializer
from backend.eprofile.models import EscortProfile, EscortImage, EscortProfileTag, EscortAvailability, Booking, Review

# Serializador para EscortImage
class EscortImageSerializer(ModelSerializer):
    class Meta:
        model = EscortImage
        fields = ['id', 'escort_profile', 'image', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']

# Serializador para EscortProfileTag
class EscortProfileTagSerializer(ModelSerializer):
    class Meta:
        model = EscortProfileTag
        fields = ['id', 'escort_profile', 'tag', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']

class EscortAvailabilitySerializer(ModelSerializer):
    class Meta:
        model = EscortAvailability
        fields = ['id', 'escort_profile', 'day_of_week', 'start_time', 'end_time', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']

# Serializador para Booking
class BookingSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'escort_profile', 'client', 'start_time', 'end_time', 'price', 'status', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']

# Serializador para Review
class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'escort_profile', 'client', 'rating', 'comment', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']

# Serializador para EscortProfile
class EscortProfileSerializer(ModelSerializer):
    availability = EscortAvailabilitySerializer(many=True, read_only=True)
    images = EscortImageSerializer(many=True, read_only=True)
    tags = EscortProfileTagSerializer(many=True, read_only=True)
    bookings = BookingSerializer(many=True, read_only=True)
    reviews = ReviewSerializer(many=True, read_only=True)


    class Meta:
        model = EscortProfile
        fields = ['id', 'user', 'title', 'description', 'is_escort', 'availability', 'location', 'images', 'tags', 'bookings', 'reviews', 'created_at', 'updated_at', 'is_active']
        read_only_fields = ['created_at', 'updated_at']