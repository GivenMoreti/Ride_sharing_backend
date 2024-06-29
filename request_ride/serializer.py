from rest_framework import serializers
from .models import RequestRide

class RequestRideSerializer(serializers.ModelSerializer):
    class Meta:
        model = RequestRide
        fields= "__all__"
