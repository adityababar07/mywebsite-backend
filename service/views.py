from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .models import Service
from .serializer import ServiceSerializer

# Create your views here.

class ServiceCreateView(ListCreateAPIView):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    
