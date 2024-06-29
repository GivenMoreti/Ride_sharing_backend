
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    
    #home page
    #path("",include('ride.urls')),
    #apis
    path('admin/', admin.site.urls),
    path("rides/",include("ride.urls")),
    path("locations/",include("location.urls")),
    path("vehicles/",include("vehicle.urls")),
]
