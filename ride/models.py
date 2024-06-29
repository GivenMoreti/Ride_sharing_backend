
from django.db import models
from django.conf import settings
from django.utils import timezone



class Ride(models.Model):
    rider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='rides_as_rider')
    driver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True, related_name='rides_as_driver')
    pickup_location = models.CharField(max_length=255)
    dropoff_location = models.CharField(max_length=255)
    pickup_date_time = models.DateTimeField()
    fare_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"A ride from {self.pickup_location} to {self.dropoff_location} fare {self.fare_amount}"
    
    def calculateTimeDifference(self):
        pickup_time_time = self.pickup_date_time.time()
        now_time = timezone.now().time()

        # Calculate time difference
        if self.pickup_date_time.date() == timezone.now().date():
            # Same date, calculate difference in time only
            time_difference = pickup_time_time - now_time
        else:
            # Different date, consider it as the next day
            time_difference = pickup_time_time - now_time + timezone.timedelta(days=1)
        return time_difference
    
    # def remove_trip_on_completion(self):
    #     if self.completed:          
    #         self.delete()
    #         return "ride deleted cause its completed"