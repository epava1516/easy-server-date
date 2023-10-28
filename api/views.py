from api.serializers.advertisement import Advertisement, AdvertisementSerializer
from api.serializers.eprofile import (
    EscortProfile, EscortProfileSerializer,
    EscortImage, EscortImageSerializer,
    EscortProfileTag, EscortProfileTagSerializer,
    EscortAvailability, EscortAvailabilitySerializer,
    Booking, BookingSerializer,
    Review, ReviewSerializer
)
from api.serializers.eventlog import EventLog, EventLogSerializer
from api.serializers.invoice import Invoice, InvoiceSerializer
from api.serializers.message import Message, MessageSerializer
from api.serializers.notification import Notification, NotificationSerializer
from api.serializers.paymentmethod import PaymentMethod, PaymentMethodSerializer
from api.serializers.tag import Tag, TagSerializer
from api.serializers.transaction import Transaction, TransactionSerializer
from api.serializers.usetting import UserSetting, UserSettingSerializer
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

# Aquí se crean las vistas.
class EscortProfileViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo EscortProfile.
    """
    queryset = EscortProfile.objects.all()
    serializer_class = EscortProfileSerializer

class EscortImageViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo EscortImage.
    """
    queryset = EscortImage.objects.all()
    serializer_class = EscortImageSerializer

class EscortProfileTagViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo EscortProfileTag.
    """
    queryset = EscortProfileTag.objects.all()
    serializer_class = EscortProfileTagSerializer

class EscortAvailabilityViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo EscortAvailability.
    """
    queryset = EscortAvailability.objects.all()
    serializer_class = EscortAvailabilitySerializer

class BookingViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo Booking.
    """
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer

class ReviewViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo Review.
    """
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class EventLogViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo EventLog.
    """
    queryset = EventLog.objects.all()
    serializer_class = EventLogSerializer

class AdvertisementViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo Advertisement.
    """
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer

class InvoiceViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo Invoice.
    """
    queryset = Invoice.objects.all()
    serializer_class = InvoiceSerializer

class MessageViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo Message.
    """
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo Notification.
    """
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer

class PaymentMethodViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo PaymentMethod.
    """
    queryset = PaymentMethod.objects.all()
    serializer_class = PaymentMethodSerializer

class TagViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo Tag.
    """
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TransactionViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo Transaction.
    """
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

class UserSettingViewSet(viewsets.ModelViewSet):
    """
    Vista para el modelo UserSetting.
    """
    queryset = UserSetting.objects.all()
    serializer_class = UserSettingSerializer
    
class SignUpView(APIView):
    """
    Vista para el registro de usuarios.
    """
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Método POST para el registro de usuarios.
        """
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        first_name = request.data.get("first_name")
        last_name = request.data.get("last_name")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if not email:
            return Response({"error": "Email is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not first_name:
            return Response({"error": "First name is required"}, status=status.HTTP_400_BAD_REQUEST)

        if not last_name:
            return Response({"error": "Last name is required"}, status=status.HTTP_400_BAD_REQUEST)
        
        user, created = User.objects.get_or_create(username=username)

        if created:
            user.set_password(password)
            user.save()
            
            EscortProfile.objects.create(user=user)
            UserSetting.objects.create(user=user)

            refresh = RefreshToken.for_user(user)

            return Response({
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": "Username already exists"}, status=status.HTTP_400_BAD_REQUEST)
