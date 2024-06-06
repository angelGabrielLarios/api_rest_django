from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def get_mock_data(request):
    data = {
        "name": "Proyecto de Prueba",
        "description": "Esto es un proyecto de prueba.",
        "status": "Activo"
    }
    return Response(data)