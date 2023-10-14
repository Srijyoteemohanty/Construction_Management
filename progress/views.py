from rest_framework import generics
from .models import progress
from .serializers import ProgressSerializer


class ProgressListCreateView(generics.ListCreateAPIView):
    queryset = progress.objects.all()
    serializer_class = ProgressSerializer

class ProgressDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = progress.objects.all()
    serializer_class = ProgressSerializer
