# serializers.py

from rest_framework import serializers
from .models import Video

class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ['file']
    
    def validate_file(self, value):
        # Validación para asegurarse de que solo se acepten archivos .mp4
        if not value.name.endswith('.mp4'):
            raise serializers.ValidationError("Only .mp4 files are allowed.")
        return value
