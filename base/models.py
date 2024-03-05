from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class TravelPackage(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField()
    destination = models.CharField(max_length=254)
    type_of_trip = models.CharField(max_length=254)
    contact_name = models.CharField(max_length=254, default="No Name")
    contact_number = models.CharField(max_length=254, default="No Number")
    start_date = models.DateField(default=timezone.localdate)
    departure_city = models.CharField(max_length=254, default="No Specified")
    end_city = models.CharField(max_length=254, default="No Specified")
    image = models.ImageField(upload_to="uploads/travel_package_images/")

    def __str__(self):
        return self.title


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name
