from django.db import models
from backend.transaction.models import Transaction
from django.conf import settings
from django.urls import reverse

# Create your models here.
# Modelo para facturación (Invoice)
class Invoice(models.Model):
    transaction = models.OneToOneField(Transaction, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    is_paid = models.BooleanField(default=False)
    invoice_pdf = models.FileField(upload_to='invoices/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Invoice'
        verbose_name_plural = 'Invoices'
        ordering = ['-issued_date']

    def __str__(self):
        return self.transaction.user.username
