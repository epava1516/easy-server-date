from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Modelo para métodos de pago (PaymentMethod)
class PaymentMethod(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    external_id = models.CharField(max_length=50)
    type = models.CharField(max_length=20)  # Ej. 'Credit Card', 'PayPal'
    last4 = models.CharField(max_length=4, null=True, blank=True)  # Últimos 4 dígitos de la tarjeta
    brand = models.CharField(max_length=20, null=True, blank=True)  # Ej. 'Visa', 'MasterCard'
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
