from django.urls import path

from . import views

app_name = 'ai'
urlpatterns = [
    path('generate_progress/', views.generate_progress, name='generate_progress'),
    path('get_SpeakingC/', views.get_SpeakingC, name='get_SpeakingC'),
]