from django.urls import path, include
from . import views

urlpatterns = [
    path('mypage/',views.mypage),
    path('update/',views.update),
    path('updateResult/',views.updateResult),
    path('unregister/',views.unregister),
    path('unResult/',views.unResult)
    ]