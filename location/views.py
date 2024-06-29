from django.shortcuts import render
from .models import Location
#location api dependencies
from rest_framework import generics
from .serializer import LocationSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view




#rest framework starts here

#Get All artists
@api_view(['GET'])
def getLocations(request):
    locations = Location.objects.all()
    serializer = LocationSerializer(locations,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getLocation(request,pk):
    existing_artist = Location.objects.get(id=pk)
    serializer = LocationSerializer(existing_artist,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createLocation(request):
    data = request.data
    new_artist = Location.objects.create(
        body = data['body']
    )
    serializer = LocationSerializer(new_artist,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateLocation(request,pk):
    data = request.data
    artist = Location.objects.get(id =pk)
    serializer = LocationSerializer(artist,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

#delete an artist
@api_view(['DELETE'])
def deleteLocation(request,pk):
    data = Location.objects.get(id=pk)
    data.delete()
    return Response("location was deleted")