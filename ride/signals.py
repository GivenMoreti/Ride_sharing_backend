from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ride

@receiver(post_save, sender=Ride)
def delete_completed_ride(sender, instance, **kwargs):
    if instance.completed:
        instance.delete()