# projects/urls.py
from django.urls import path
from .views import generate_minutes_of_video_meeting, VideoUploadView


urlpatterns = [

    path('generate-minutes-of-video-meeting', generate_minutes_of_video_meeting, name='generate_minutes_of_video_meeting'),
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
]
