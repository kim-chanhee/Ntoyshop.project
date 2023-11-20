from django.urls import path
from . import views

urlpatterns = [
    path('',views.payment),
    path('checkpay/',views.checkpay),
    path('payresult/',views.payresult),
]