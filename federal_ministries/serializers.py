from rest_framework import serializers
from .models import FederalMinistry

class FederalMinistrySerializer(serializers.ModelSerializer):
    class Meta:
        model = FederalMinistry
        fields = '__all__'