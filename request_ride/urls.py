from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
  
    path("",views.getRideRequests,name = "get-rides-requests"),
    path("create/",views.createRideRequest,name = "create-ride-request"),
    path("<str:pk>/",views.getRideRequest,name = "get-ride-request"),
    path("<str:pk>/update/",views.updateRideRequest,name = "update-ride-request"),
    path("<str:pk>/delete/",views.deleteRideRequest,name = "delete-ride-request"),
]
