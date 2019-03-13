from rest_framework import serializers
from .models import University

class UniversitiesSerializers(serializers.ModelSerializer):
    class Meta:
        model = University
        fields = '__all__'
