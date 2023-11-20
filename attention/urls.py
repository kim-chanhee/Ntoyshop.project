from django.contrib import admin
from django.urls import path
from . import views



urlpatterns = [
    path('attend/',views.attend),
    path('produce/',views.produce),
    path('date/',views.date),
    path('chk/',views.chk),
    path('show/',views.show),
    path('showtable/',views.showtable),

]