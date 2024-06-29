from django.db import models
from django.conf import settings

# Create your models here.
class Vehicle(models.Model):
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='vehicles')
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    license_plate = models.CharField(max_length=20)
    
    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.license_plate}) for {self.driver}"