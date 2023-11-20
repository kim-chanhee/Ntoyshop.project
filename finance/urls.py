from django.contrib import admin
from django.urls import path,include
from . import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.flist),
    path('list/',views.list),
    path('salary/',views.salary),
    path('salaryResult/<int:no>',views.salaryResult),
    path('manage/',views.manage),
    path('sDelete/',views.sDelete),
    path('t/',views.t)
]