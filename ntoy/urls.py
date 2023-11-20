"""ntoy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('member/',include('member.urls')),
    path('login/',include('login.urls')),
    path('mypage/',include('mypage.urls')),
    path('manager/',include('manager.urls')),
    path('browse/',include('browse.urls')),
    path('pay/',include('pay.urls')),
    path('summernote/', include('django_summernote.urls')),
    path('basket/',include('basket.urls')),
    path('attention/',include('attention.urls')),
    path('finance/',include('finance.urls')),
    path('search/',include('search.urls')),
    path('order/',include('order.urls')),
    path('board/',include('board.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)