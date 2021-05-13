from django.urls import path
from django.conf import settings
from .views import ProjectCreateView, ProjectListView
from django.conf.urls.static import static

urlpatterns = [
    # path('', HomepageView.as_view(), name = "home"),
    path('project/create', ProjectCreateView.as_view(), name="project_create"),
    path('project/', ProjectListView.as_view(), name='project_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
