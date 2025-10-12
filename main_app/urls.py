from django.urls import path
from . import views

urlpatterns = [
    #homepage
    path('', views.HomepageView.as_view(), name='home'),
    
    #Company
    path('company/company_list.html', views.CompanyListView.as_view(), name='company_list'),
    path('company/<int:id>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('company/create/', views.CompanyCreateView.as_view(), name='company_form'),
    path('company/<int:id>/update', views.CompanyUpdateView.as_view(), name='company_update'),
    path('company/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),

    #Car
    path('car/car_list.html', views.CarListView.as_view(), name='car_list'),
    path('car/<int:id>/', views.CarDetailView.as_view(), name='car_detail'),
    path('car/create/', views.CarCreateView.as_view(), name='car_form'),
    path('car/<int:id>/update', views.CarUpdateView.as_view(), name='car_update'),
    path('car/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),

    #Contact
    path('contact/company_list.html', views.ContactListView.as_view(), name='contact_list'),
    path('contact/<int:id>/', views.ContactDetailView.as_view(), name='contact_detail'),
    path('contact/create/', views.ContactCreateView.as_view(), name='contact_form'),
    path('contact/<int:id>/update', views.ContactUpdateView.as_view(), name='contact_update'),
    path('contact/<int:pk>/delete/', views.ContactDeleteView.as_view(), name='contact_delete'),
]