from django.urls import path
from django.conf import settings
from .views import HomepageView, ProjectCreateView, ProjectDetailView
from django.conf.urls.static import static

urlpatterns = [
    path('project/<int:pk>/', ProjectDetailView.as_view(), name="project_detail"),
    path('project/', ProjectCreateView.as_view(), name="project_create"),
    path('', HomepageView.as_view(), name = "home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
