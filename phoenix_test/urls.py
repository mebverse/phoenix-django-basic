from core.views import health, home
from django.urls import path

urlpatterns = [
    path("", home),
    path("health/", health),
]
