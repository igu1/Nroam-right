from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class Destination(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='destination_images')

    def __str__(self):
        return self.name


class Agencie(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='agency')
    agency_name = models.CharField(max_length=100)
    admin_name = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    business_address = models.TextField()
    company_description = models.TextField()
    website_link = models.URLField()
    image = models.ImageField(
        upload_to='uploads/agencies/', null=True, blank=True)
    blog = RichTextField('Blog', blank=True, null=True)

    def __str__(self):
        return self.agency_name


class TravelPackage(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField(null=True, blank=True)
    agency = models.ForeignKey(Agencie, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    duration_days = models.IntegerField()
    destination = models.CharField(max_length=254)
    type_of_trip = models.CharField(max_length=254)
    contact_name = models.CharField(max_length=254, default='No Name')
    contact_number = models.CharField(max_length=254, default='No Number')
    start_date = models.DateField(default=timezone.localdate)
    departure_city = models.CharField(max_length=254, default='No Specified')
    end_city = models.CharField(max_length=254, default='No Specified')
    image = models.ImageField(upload_to='uploads/travel_package_images/')

    def __str__(self):
        return self.title


class FeaturedPackage(models.Model):
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)

    def __str__(self):
        return self.package.title


class AgencyReview(models.Model):
    for_agency = models.ForeignKey(Agencie, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    review = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username + ' --> ' + self.for_agency.title


class Reservation(models.Model):
    package = models.ForeignKey(TravelPackage, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    number = models.CharField(max_length=12)
    adult = models.IntegerField()
    kids = models.IntegerField()
    date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return self.name


class NewsLetter(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField()

    def __str__(self):
        return self.email
