from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Modelo para transacciones (Transaction)
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('credit_purchase', 'Purchase of Credits'),
        ('profile_highlight', 'Profile Highlight'),
        ('booking', 'Booking'),
        ('booking_cancellation', 'Booking Cancellation'),
        ('booking_completion', 'Booking Completion'),
        # ('booking_refund', 'Booking Refund'),
        ('booking_reschedule', 'Booking Reschedule'),
        ('booking_reschedule_cancellation', 'Booking Reschedule Cancellation'),
        ('booking_reschedule_completion', 'Booking Reschedule Completion'),
        # ('booking_reschedule_refund', 'Booking Reschedule Refund'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('failed', 'Failed'),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    currency = models.CharField(max_length=3)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    payment_method = models.CharField(max_length=50)
    external_id = models.CharField(max_length=50, null=True, blank=True)
    is_successful = models.BooleanField(default=False)
    payment_gateway_response = models.JSONField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
# Mirar ideas de cancelacción y refund en chatgpt
# https://chat.openai.com/c/674e08fd-d044-477b-a1d6-9b6b077eb185