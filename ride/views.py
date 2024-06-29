from django.shortcuts import render, get_object_or_404
from .models import Ride
#location api dependencies
from rest_framework import generics
from .serializer import RideSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.utils.timezone import now
from datetime import timedelta
from django.utils import timezone

def home_page(request):
    get_rides = Ride.objects.all()
    # pickup_time = Ride.pickup_time
    # created_at = Ride.created_at
    # latest_ride =Ride.objects.latest('created_at')
    time_difference = Ride.calculateTimeDifference
    print(time_difference)
    context = {"get_rides":get_rides}
    
    return render(request,"ride/home.html",context)

#rest framework starts here

#Get All artists
@api_view(['GET'])
def getRides(request):
    rides = Ride.objects.all()
    serializer = RideSerializer(rides,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRide(request,pk):
    existing_ride = Ride.objects.get(id=pk)
    serializer = RideSerializer(existing_ride,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createRide(request):
    data = request.data
    new_ride = Ride.objects.create(
        body = data['body']
    )
    serializer = RideSerializer(new_ride,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateRide(request,pk):
    data = request.data
    ride = Ride.objects.get(id =pk)
    serializer = RideSerializer(ride,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#delete an artist
@api_view(['DELETE'])
def deleteRide(request,pk):
    data = Ride.objects.get(id=pk)
    data.delete()
    return Response("ride was deleted")