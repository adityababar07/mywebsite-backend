from django.forms import ModelForm      
from .models import Project

class PhotoForm(ModelForm):
  class Meta:
      model = Project
