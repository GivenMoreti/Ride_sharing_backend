from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("rides/home/",views.home_page,name="home-page"),
    path("",views.getRides,name = "get-rides"),
    path("create/",views.createRide,name = "create-ride"),
    path("<str:pk>/",views.getRide,name = "get-ride"),
    path("<str:pk>/update/",views.updateRide,name = "update-ride"),
    path("<str:pk>/delete/",views.deleteRide,name = "delete-ride"),
]
