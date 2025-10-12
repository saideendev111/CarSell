from django.urls import path
from . import views

urlpatterns = [
    #homepage
    path('', views.HomepageView.as_view(), name='home'),
    
]