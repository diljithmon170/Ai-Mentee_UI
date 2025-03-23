from django.urls import path
from . import views  # ✅ Import views from the current app (dashboard)

urlpatterns = [
    path('', views.dashboard, name='dashboard'),  # Dashboard view
    path('level/', views.level, name='level'),  # Level selection view
    path('quiz/', views.quiz, name='quiz'),  # ✅ Quiz page route
]
