from django.urls import path


from .views import ProgressDetailView, ProgressListCreateView

urlpatterns = [
    path('progress/', ProgressListCreateView.as_view(), name='progress-list-create'),
    path('progress/<int:pk>/', ProgressDetailView.as_view(), name='progress-detail'),
]