from django.urls import path
from . import views

urlpatterns = [

    path("",views.getProfiles,name = "get-profiles"),
    path("create/",views.createProfile,name = "create-profile"),
    path("<str:pk>/",views.getProfile,name = "get-profile"),
    path("<str:pk>/update/",views.updateProfile,name = "update-profile"),
    path("<str:pk>/delete/",views.deleteProfile,name = "delete-profile"),
]
