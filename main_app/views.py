from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Car, Company, Contact
from .forms import CarForm, CompanyForm, ContactForm

#cbv imports
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

# Create your views here.

#CRUD for company
class CompanyListView(ListView):
    model = Company
    template_name = 'company/company_list.html'
    context_object_name = 'companies'

class CompanyDetailView(DetailView):
    model = Company
    template_name = 'company/company_detail.html'
    context_object_name = 'company'

class CompanyCreateView(CreateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_form.html'
    success_url = reverse_lazy('company_list')

class CompanyUpdateView(UpdateView):
    model = Company
    form_class = CompanyForm
    template_name = 'company/company_form.html'
    success_url = reverse_lazy('company_list')

class CompanyDeleteView(DeleteView):
    model = Company
    success_url = reverse_lazy('company_list')

#Crud for car
class CarListView(ListView):
    model = Car
    template_name = 'car/car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car/car_detail.html'
    context_object_name = 'car'
    pk_url_kwarg = 'id'

class CarCreateView(CreateView):
    model = Car
    form_class = CarForm
    template_name = 'car/car_form.html'
    success_url = reverse_lazy('car_list')

class CarUpdateView(UpdateView):
    model = Car
    form_class = CarForm
    template_name = 'car/car_form.html'
    success_url = reverse_lazy('car_list')

class CarDeleteView(DeleteView):
    model = Car
    success_url = reverse_lazy('car_list')

#CRUD for contact
class ContactListView(ListView):
    model = Contact
    template_name = 'contact/contact_list.html'
    context_object_name = 'contacts'

class ContactDetailView(DetailView):
    model = Contact
    template_name = 'contact/contact_detail.html'
    context_object_name = 'contacts'

class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    template_name = 'contact/contact_form.html'
    success_url = reverse_lazy('contact_list.html')

class ContactDeleteView(DeleteView):
    model = Contact
    success_url =  reverse_lazy('contact_list.html')