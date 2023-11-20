from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.browse),
    path('basketinfo/',views.basketinfo),
    path('basket/',views.basket),
    path('delete/',views.delete),
    
    ]
