from django.db import models
from ride.models import Ride
from user_profile.models import UserProfile


# Create your models here.
class RequestRide(models.Model):
    ride = models.ForeignKey(Ride,on_delete=models.CASCADE)
    #who made the request
    passenger = models.ForeignKey(UserProfile,on_delete=models.CASCADE,null=True)
    time_requested = models.DateTimeField(auto_now_add=True)
    time_edited = models.DateTimeField(auto_now=True)
    cancel_request = models.BooleanField(default=False)     #if user changes to True request is aborted
    

    def __str__(self):
        return f"Ride {str(self.ride)} request made at {str(self.time_requested)}"
    
    def delete_request_on_cancel(self):
        if self.cancel_request:
            self.delete() #add signals for this

