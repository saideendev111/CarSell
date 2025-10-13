from django import forms
from .models import Car, Company, Contact

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['company_name']

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['car_model', 'company','car_type', 'year', 'price', 'description','contact']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['contact_name', 'phone_num']