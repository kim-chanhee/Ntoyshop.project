
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.browse),
    path('show/',views.show),
    path('page/',views.page),
    path('/board/',include('board.urls'))
    ]