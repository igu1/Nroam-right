from django.contrib import admin
from .models import (
    TravelPackage,
    Contact,
)

admin.site.register(Contact)
admin.site.register(TravelPackage)
