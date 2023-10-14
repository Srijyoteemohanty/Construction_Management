from django.urls import path


from .views import AttendanceDetailView, AttendanceListCreateView

urlpatterns = [
    path('attendance/', AttendanceDetailView.as_view(), name='attendance-list-create'),
    path('attendance/<int:pk>/', AttendanceListCreateView.as_view(), name='attendance-detail'),
]