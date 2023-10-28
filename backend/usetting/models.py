from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# Modelo para configuración de usuario (UserSetting)

# NOTIFICATION_CHOICES = [
#     ('all', 'All'),
#     ('important', 'Important Only'),
#     ('none', 'None'),
# ]

class UserSetting(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='settings')
    receive_notifications = models.BooleanField(default=True)
    discreet_notifications = models.BooleanField(default=False)
    # preferred_language = models.CharField(max_length=10, null=True, blank=True)
    time_zone = models.CharField(max_length=50, null=True, blank=True)
    ui_mode = models.CharField(max_length=50, choices=[('light', 'Light'), ('dark', 'Dark')], default='light')
    email_frequency = models.CharField(max_length=50, choices=[('daily', 'Daily'), ('weekly', 'Weekly'), ('none', 'None')], default='none')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
