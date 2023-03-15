from django.forms import ModelForm
from .models import Reservation, Contact


class ReservationForm(ModelForm):
    class Meta:
        model = Reservation
        fields = ['name', 'email', 'number',
                  'adult', 'kids', 'date', 'message']


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
