from rest_framework import routers
from api.views import (
    EscortProfileViewSet,
    EscortImageViewSet,
    EscortProfileTagViewSet,
    EscortAvailabilityViewSet,
    BookingViewSet,
    ReviewViewSet,
    EventLogViewSet,
    AdvertisementViewSet,
    InvoiceViewSet,
    MessageViewSet,
    NotificationViewSet,
    PaymentMethodViewSet,
    TagViewSet,
    TransactionViewSet,
    UserSettingViewSet,
)

router = routers.DefaultRouter()

# User api
router.register(r'profiles', EscortProfileViewSet)
router.register(r'escort-images', EscortImageViewSet)
router.register(r'escort-profile-tags', EscortProfileTagViewSet)
router.register(r'escort-availabilities', EscortAvailabilityViewSet)
router.register(r'bookings', BookingViewSet)
router.register(r'reviews', ReviewViewSet)
router.register(r'event-logs', EventLogViewSet)
router.register(r'advertisements', AdvertisementViewSet)
router.register(r'invoices', InvoiceViewSet)
router.register(r'messages', MessageViewSet)
router.register(r'notifications', NotificationViewSet)
router.register(r'payment-methods', PaymentMethodViewSet)
router.register(r'tags', TagViewSet)
router.register(r'transactions', TransactionViewSet)
router.register(r'user-settings', UserSettingViewSet)

urlpatterns = router.urls
