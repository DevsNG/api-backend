from rest_framework import generics
from .models import Airport
from .serializers import AirportsSerializers


# Create your views here.

class AirportsList(generics.ListAPIView):
    serializer_class = AirportsSerializers
    queryset = Airport.objects.all().order_by('name')
    filter_fields = ('type', 'established', 'state',)
    ordering_fields = ('name', 'established', 'state')
    search_fields = ('name',)


class AirportDetail(generics.RetrieveAPIView):
    serializer_class = AirportsSerializers
    queryset = Airport.objects.all()
    lookup_field = 'name'
    #lookup_url_kwarg = 'name'

