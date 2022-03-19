from django import forms
from django.forms import ModelForm
from .models import Venue, Event


# create forms


class Eventform(ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'manager', 'attendees', 'description',)

        labels = {
            'name': '',
            'event_date': 'YYYY-MM-DD HH:MM:SS ',
            'venue': 'Venue',
            'manager': 'Manager',
            'attendees': 'Attendees',
            'description': 'Description',

        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event name'}),
            'event_date':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Event date'}),
            'venue': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Event venue'}),
            'manager': forms.Select(attrs={'class': 'form-select', 'placeholder': 'Manager'}),
            'attendees': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder': 'Attendees'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Description'}),

        }


class Venueform(ModelForm):
    class Meta:
        model = Venue
        fields = ('name','region', 'address', 'zip_code', 'website', 'phone_number', 'email_address',)

        labels = {

            'name': '',
            'region':'',
            'address': '',
            'zip_code': '',
            'website': '',
            'phone_number': '',
            'email_address': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Venue name'}),
            'region': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Region (former provinces)'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'zip_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Zip code'}),
            'website': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Website'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address'}),

        }
