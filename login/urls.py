from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.login),
    path('checkLogin/',views.checkLogin),
    path('logout/',views.logout),
    ]