from rest_framework import serializers
from .models import Airport

class AirportsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = '__all__'
