from django.urls import path
from .views import ProjectListCreateView, ProjectDetailView

urlpatterns = [
    path('api/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('api/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
]