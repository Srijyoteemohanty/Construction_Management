from rest_framework import generics
from .models import attendance
from .serializers import AttendanceSerializer


class AttendanceListCreateView(generics.ListCreateAPIView):
    queryset = attendance.objects.all()
    serializer_class = AttendanceSerializer

class AttendanceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = attendance.objects.all()
    serializer_class = AttendanceSerializer