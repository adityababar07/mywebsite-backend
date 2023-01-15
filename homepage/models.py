from django.db import models
from django.urls import reverse
import cloudinary
# Create your models here.


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=50)
    project_description = models.TextField(max_length=500)
    project_image = models.ImageField(upload_to="project_screenshot/") 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.project_name

    def get_absolute_url(self):
        return reverse('project_detail', args=[str(self.pk)])
