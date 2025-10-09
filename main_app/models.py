from django.db import models

# Create your models here.

class Company(models.Model):
    company_id = models.BigAutoField(primary_key=True)
    company_name = models.CharField(max_length=100, null=False)

    def __str__(self):
        return self.company_name    

class Contact(models.Model):
    contact_id = models.BigAutoField(primary_key=True)
    contact_name = models.CharField(max_length=100, null=False)
    phone_num = models.IntegerField(null=False)

    def __str__(self):
        return self.contact_name

class Car(models.Model):
    CAR_TYPES = [
        ('Sedan', 'Sedan'),
        ('Coupe', 'Coupe'),
        ('SUV', 'SUV'),
        ('Hatchback', 'Hatchback'),
    ]

    car_id = models.BigAutoField(primary_key=True)
    car_model = models.CharField(max_length=100, null=False)
    car_type = models.CharField(max_length=30, choices=CAR_TYPES)
    year = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, related_name='cars', null=True)
    contact = models.ForeignKey(Contact, on_delete=models.SET_NULL, related_name='cars', null=True)

    def __str__(self):
        return f"{self.car_model} ({self.year})"
    