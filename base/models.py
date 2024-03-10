from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver

class Location(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
class Destination(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = RichTextField(null=True, blank=True)
    location = models.ForeignKey(
        Location, on_delete=models.CASCADE, null=True, blank=True
    )
    def __str__(self):
        return self.name


class TravelPackage(models.Model):
    title = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    description = RichTextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField()
    image = models.ImageField(upload_to="uploads/travel_package_images/")
    destinations = models.ManyToManyField(Destination, related_name="destinations")

    def __str__(self):
        return self.title.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
