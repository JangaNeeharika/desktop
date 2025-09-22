from django import forms
from .models import DemoClassRegistration
from .models import GeneralDonation
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'contact_number', 'email', 'message']
class GeneralDonationForm(forms.ModelForm):
    class Meta:
        model = GeneralDonation
        fields = ['name', 'email', 'items', 'image', 'delivery']

class DonationForm(forms.ModelForm):
    class Meta:
        model = GeneralDonation
        fields = ['name', 'email', 'address', 'items', 'image', 'delivery']
        
class DemoClassForm(forms.ModelForm):
    class Meta:
        model = DemoClassRegistration
        fields = ['name', 'email', 'skills', 'message']
