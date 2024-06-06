# projects/urls.py
from django.urls import path
from .views import get_mock_data

urlpatterns = [
    path('api/mock-data/', get_mock_data, name='get_mock_data'),
]
