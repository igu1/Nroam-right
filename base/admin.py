from django.contrib import admin
from .models import Destination, TravelPackage, FeaturedPackage, AgencyReview, Reservation, Agencie, Contact, NewsLetter


admin.site.register(Destination)
admin.site.register(NewsLetter)
admin.site.register(AgencyReview)
admin.site.register(Reservation)
admin.site.register(FeaturedPackage)
admin.site.register(Contact)


class AgencyAdmin(admin.ModelAdmin):

    def get_form(self, request, obj=None, **kwargs):
        self.exclude = []
        if not request.user.is_superuser:
            self.exclude.append('agency_name')
            self.exclude.append('user')
        return super(AgencyAdmin, self).get_form(request, obj, **kwargs)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Show all records to staff users
        else:
            return qs.filter(agency_name=request.user.username)


admin.site.register(Agencie, AgencyAdmin)


class TravelPackageAdmin(admin.ModelAdmin):
    exclude = ('agency',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs  # Show all records to staff users
        else:
            return qs.filter(agency__agency_name=request.user.username)

    def save_model(self, request, obj, form, change):
        # access the data before saving
        data = form.cleaned_data
        agency = data.get('agency')

        # modify the object before saving
        obj.agency = Agencie.objects.get(user=request.user)

        super().save_model(request, obj, form, change)


admin.site.register(TravelPackage, TravelPackageAdmin)
