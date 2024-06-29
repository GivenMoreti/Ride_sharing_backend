from django.shortcuts import render, get_object_or_404
from .models import RequestRide
from rest_framework import generics
from .serializer import RideSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.utils.timezone import now
from datetime import timedelta
from django.utils import timezone



#rest framework starts here

@api_view(['GET'])
def getRideRequests(request):
    requests = RequestRide.objects.all()
    serializer = RideSerializer(requests,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getRequest(request,pk):
    existing_request = RequestRide.objects.get(id=pk)
    serializer = RideSerializer(existing_request,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createRideRequest(request):
    data = request.data
    new_ride = RequestRide.objects.create(
        body = data['body']
    )
    serializer = RideSerializer(new_ride,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateRide(request,pk):
    data = request.data
    ride = RequestRide.objects.get(id =pk)
    serializer = RideSerializer(ride,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteRide(request,pk):
    data = RequestRide.objects.get(id=pk)
    data.delete()
    return Response("ride request was deleted")