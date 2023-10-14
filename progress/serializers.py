from rest_framework import serializers
from .models import progress

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = progress
        fields = '__all__'
