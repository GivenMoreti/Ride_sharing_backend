from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ride

@receiver(post_save, sender=Ride)
def delete_completed_ride(sender, instance, **kwargs):
    if instance.completed:
        instance.delete()


@receiver(post_save, sender=Ride)
def remove_from_requests(sender,instance,**kwargs):
    if instance.is_fully_booked:
        instance.delete()