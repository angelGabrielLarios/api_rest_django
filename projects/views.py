from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from.models import ModelVideoIndexer
from dotenv import load_dotenv
import os

load_dotenv()
@api_view(['GET'])
def get_video_transcript(request):
    angel = os.getenv('angel')
    print(angel)
    return Response(ModelVideoIndexer())