from rest_framework import serializers
from .models import assets

class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = assets
        fields = '__all__'
