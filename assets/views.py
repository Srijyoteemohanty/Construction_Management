from rest_framework import generics
from .models import assets
from .serializers import AssetSerializer


class AssetListCreateView(generics.ListCreateAPIView):
    queryset = assets.objects.all()
    serializer_class = AssetSerializer

class AssetDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = assets.objects.all()
    serializer_class = AssetSerializer
