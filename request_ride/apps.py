from django.apps import AppConfig


class RequestRideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'request_ride'

    def ready(self):
        import request_ride.signals