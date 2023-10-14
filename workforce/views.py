from rest_framework import generics
from .models import workforce
from .serializers import WorkforceSerializer


class WorkforceListCreateView(generics.ListCreateAPIView):
    queryset = workforce.objects.all()
    serializer_class = WorkforceSerializer

class WorkforceDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = workforce.objects.all()
    serializer_class = WorkforceSerializer

