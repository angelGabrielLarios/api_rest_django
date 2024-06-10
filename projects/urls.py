# projects/urls.py
from django.urls import path
from .views import get_video_transcript

urlpatterns = [
    path('api/get-video-transcript/', get_video_transcript, name='api/get_video_transcript'),
]
