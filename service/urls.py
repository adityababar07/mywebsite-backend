from django.urls import path
from .views import ServiceCreateView

urlpatterns = [
    path('api/v1/service/', ServiceCreateView.as_view(), name='service'),
]
