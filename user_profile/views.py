from django.shortcuts import render, get_object_or_404
from .models import UserProfile
#location api dependencies
from rest_framework import generics
from .serializer import UserProfileSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.utils.timezone import now
from datetime import timedelta
from django.utils import timezone



#rest framework starts here


@api_view(['GET'])
def getProfiles(request):
    rides = UserProfile.objects.all()
    serializer = UserProfileSerializer(rides,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProfile(request,pk):
    existing_ride = UserProfile.objects.get(id=pk)
    serializer = UserProfileSerializer(existing_ride,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createProfile(request):
    data = request.data
    new_ride = UserProfile.objects.create(
        body = data['body']
    )
    serializer = UserProfileSerializer(new_ride,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateProfile(request,pk):
    data = request.data
    ride = UserProfile.objects.get(id =pk)
    serializer =UserProfileSerializer(ride,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#delete an artist
@api_view(['DELETE'])
def deleteProfile(request,pk):
    data = UserProfile.objects.get(id=pk)
    data.delete()
    return Response("ride was deleted")