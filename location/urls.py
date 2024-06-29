
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.getLocations,name = "get-locations"),
    path("create/",views.createLocation,name = "create-location"),
    path("<str:pk>/",views.getLocation,name = "get-location"),
    path("<str:pk>/update/",views.updateLocation,name = "update-location"),
    path("<str:pk>/delete/",views.deleteLocation,name = "delete-location"),
]
