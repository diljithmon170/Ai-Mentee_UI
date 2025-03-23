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
    path('text/<str:level>/', views.text_view, name='text'),  # Text page with level parameter
    path('content/<str:level>/', views.content_view, name='content'), # Content page with level parameter

    path('text/<str:level>/', views.text_view, name='text'),
    path('audio/<str:level>/', views.audio_view, name='audio'),
    path('video/<str:level>/', views.video_view, name='video'),

    path('text/<str:level>/<int:file_number>/', views.text_view, name='text'),
    path('video/<str:level>/<int:file_number>/', views.video_view, name='video'),
    path('audio/<str:level>/<int:file_number>/', views.audio_view, name='audio'),

]