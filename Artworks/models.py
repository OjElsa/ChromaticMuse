from django.db import models
from django.utils import timezone

# Create your models here.

class Artwork(models.Model):
    title = models.CharField(max_length=100)
    artist = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='artwork_images/')
    description = models.TextField()
    daily_views = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    date_created = models.DateTimeField(default=timezone.now)
    

class Artist(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
