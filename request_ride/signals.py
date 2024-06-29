from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import RequestRide

@receiver(post_save, sender=RequestRide)
def delete_completed_ride(sender, instance, **kwargs):
    if instance.cancel_request:
        instance.delete()

