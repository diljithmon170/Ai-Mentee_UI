from get_std.views import home
from log_sig.views import log_sig
from dashboard.views import dashboard
from django.urls import path
from . import views
from django.shortcuts import render




urlpatterns = [
    
    path('', home),
    path('/log_sig/', views.log_sig,name='log_sig'),
    path('dashboard/', views.dashboard,name='dashboard'),
]