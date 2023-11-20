from django.urls import path, include
from . import views

urlpatterns = [
    path('join/',views.join),
    path('checkJoin/',views.checkJoin),
    path('login/',views.login),
]

