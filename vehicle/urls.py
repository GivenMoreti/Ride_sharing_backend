from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.getVehicles,name = "get-vehicles"),
    path("create/",views.createVehicle,name = "create-vehicle"),
    path("<str:pk>/",views.getVehicle,name = "get-vehicle"),
    path("<str:pk>/update/",views.updateVehicle,name = "update-vehicle"),
    path("<str:pk>/delete/",views.deleteVehicle,name = "delete-vehicle"),
]
