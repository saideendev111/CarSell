from django.contrib import admin
from .models import Car, Company, Contact

# Register your models here.

admin.site.register(Car)
admin.site.register(Company)
admin.site.register(Contact)