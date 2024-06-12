# projects/urls.py
from django.urls import path
from .views import generate_minutes_of_video_meeting

urlpatterns = [
    
    path('generate-minutes-of-video-meeting', generate_minutes_of_video_meeting, name='generate_minutes_of_video_meeting')

]
