from django.contrib import admin
from .models import (
    TravelPackage,
    Contact,
    Destination,
    Location
)

admin.site.register(Contact)
admin.site.register(TravelPackage)
admin.site.register(Destination)
admin.site.register(Location)