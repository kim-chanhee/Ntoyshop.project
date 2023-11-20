from django.urls import path,include
from . import views

urlpatterns = [
    # path('',views.browse),
    path('',views.order),
    path('delete/',views.delete),
    path('manage/',views.manage),
    path('delUpdate/',views.delUpdate),
    path('delDelete/',views.delDelete),
    path('returns/',views.returns),
    path('returnsResult/',views.returnsResult),
    path('reDelete/',views.reDelete)
    ]