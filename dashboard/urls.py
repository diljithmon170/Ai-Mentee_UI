from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard page
    path('level/<str:course>/', views.level, name='level'),  # Level page with course parameter
    path('quiz/<str:course>/', views.quiz_view, name='quiz'),  # Quiz page with course parameter
    path('content/<str:course>/<str:level>/', views.content_view, name='content'),  # Content page

    # Updated paths to include `course`
    path('text/<str:course>/<str:level>/', views.text_view, name='text'),  
    path('audio/<str:course>/<str:level>/', views.audio_view, name='audio'),
    path('video/<str:course>/<str:level>/', views.video_view, name='video'),

    # File-specific URLs for text, audio, and video
    path('text/<str:course>/<str:level>/<int:file_number>/', views.text_view, name='text'),

    path('video/<str:course>/<str:level>/<int:file_number>/', views.video_view, name='video'),
    path('audio/<str:course>/<str:level>/<int:file_number>/', views.audio_view, name='audio'),
]



