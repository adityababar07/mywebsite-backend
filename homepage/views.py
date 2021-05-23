from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializer import ProjectSerializer
from .models import Project
from django.urls import reverse_lazy
# Create your views here.


class HomepageView(TemplateView):
    template_name = "home.html"


class ProjectCreateView(ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
