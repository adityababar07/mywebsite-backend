from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, ListAPIView
from .serializer import ProjectSerializer
from .models import Project
# Create your views here.

class ProjectCreateView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectListView(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
