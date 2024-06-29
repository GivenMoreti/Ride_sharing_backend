from django.shortcuts import render
from .models import Vehicle
#location api dependencies
from rest_framework import generics
from .serializer import VehicleSerializer
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def getVehicles(request):
    vehicles = Vehicle.objects.all()
    serializer = VehicleSerializer(vehicles,many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getVehicle(request,pk):
    existing_vehicle = Vehicle.objects.get(id=pk)
    serializer = VehicleSerializer(existing_vehicle,many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createVehicle(request):
    data = request.data
    new_vehicle = Vehicle.objects.create(
        body = data['body']
    )
    serializer = VehicleSerializer(new_vehicle,many=False)
    return Response(serializer.data)



@api_view(['PUT'])
def updateVehicle(request,pk):
    data = request.data
    vehicle = Vehicle.objects.get(id =pk)
    serializer = VehicleSerializer(vehicle,data = request.POST)
    if(serializer.is_valid()):
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteVehicle(request,pk):
    data = Vehicle.objects.get(id=pk)
    data.delete()
    return Response("vehicle was deleted")