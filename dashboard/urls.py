from get_std.views import home
from log_sig.views import log_sig
from dashboard.views import dashboard
from django.urls import path, include
from . import views
from django.shortcuts import render
from .views import quiz_view

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard page
    path('level/<str:course>/', views.level, name='level'),  # Level page with course parameter
    path('quiz/<str:course>/', views.quiz_view, name='quiz'),  # Quiz page with course parameter
]