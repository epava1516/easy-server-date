from django.db import models

# Create your models here.
# Modelo para anuncios (Advertisement)
class Advertisement(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='ads/')
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    target_location = models.CharField(max_length=100, null=True, blank=True)
    target_user_type = models.CharField(max_length=50, choices=[('all', 'All Users'), ('escort', 'Escorts'), ('client', 'Clients')], default='all')
    clicks = models.IntegerField(default=0)
    impressions = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
