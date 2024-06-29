from django.db import models
from django.contrib.auth.models import User
from location.models import Location


# Create your models here.
class UserProfile(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to="userprofilepics")
    user_location = models.ForeignKey(Location,on_delete=models.CASCADE)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)


    def __str__(self):
        return f"{self.user.username} created on {str(self.time_created)}"
