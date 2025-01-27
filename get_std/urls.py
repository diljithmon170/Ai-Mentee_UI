"""
URL configuration for Ai_Mentee project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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

from get_std.views import home
from log_sig.views import log_sig
from dashboard.views import dashboard
from django.urls import path
from . import views
from django.shortcuts import render




urlpatterns = [
    
    path('', home),
    path('log_sig/', views.log_sig,name='log_sig'),
    path('dashboard/', views.dashboard,name='dashboard'),
]
