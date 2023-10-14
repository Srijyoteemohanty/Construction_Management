from rest_framework import serializers
from .models import workforce

class WorkforceSerializer(serializers.ModelSerializer):
    class Meta:
        model = workforce
        fields = '__all__'
