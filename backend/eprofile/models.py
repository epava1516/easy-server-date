from django.db import models
from django.db.models import Avg
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from backend.tag.models import Tag

# Create your models here.
# Modelo para el perfil de Escort
class EscortProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='escort_profile')
    is_escort = models.BooleanField(default=False)
    description = models.TextField()
    # Expected format: [{'day': 'Monday', 'from': '09:00', 'to': '17:00'}, {...}]
    # availability = models.JSONField(null=True, blank=True)
    # Expected format: {'latitude': xx.xxxx, 'longitude': yy.yyyy}
    location = models.JSONField(null=True, blank=True, default=dict)
    tags = models.ManyToManyField(Tag, through='EscortProfileTag')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
    def average_rating(self):
        reviews = Review.objects.filter(escort_profile=self)
        return reviews.aggregate(Avg('rating'))['rating__avg'] or 0.0

# Modelo para la galería de imágenes de un perfil de Escort
class EscortImage(models.Model):
    escort_profile = models.ManyToManyField(EscortProfile, related_name='images')
    # escort_profile = models.ForeignKey(EscortProfile, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    sha256 = models.CharField(max_length=64, unique=True, null=True, blank=True)  # For deduplication
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

# Relación entre EscortProfile y Tag
class EscortProfileTag(models.Model):
    escort_profile = models.ForeignKey(EscortProfile, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

class EscortAvailability(models.Model):
    escort_profile = models.ForeignKey(EscortProfile, on_delete=models.CASCADE)
    day_of_week = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(6)])  # 0=Monday, 1=Tuesday, etc.
    start_time = models.TimeField()
    end_time = models.TimeField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

# Modelo para reservas (Booking)
class Booking(models.Model):
    escort_profile = models.ForeignKey(EscortProfile, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # duration = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=50, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('completed', 'Completed'), ('cancelled', 'Cancelled')], default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    
# Modelo para calificaciones y reseñas (Review)
class Review(models.Model):
    escort_profile = models.ForeignKey(EscortProfile, on_delete=models.CASCADE)
    client = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ('escort_profile', 'client',)


# import hashlib

# def calculate_sha256(file_path):
#     sha256_hash = hashlib.sha256()
#     with open(file_path, "rb") as f:
#         # Leer solo 4K a la vez para evitar uso excesivo de memoria
#         for byte_block in iter(lambda: f.read(4096), b""):
#             sha256_hash.update(byte_block)
#     return sha256_hash.hexdigest()