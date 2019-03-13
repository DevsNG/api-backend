from rest_framework import generics
from .models import FederalMinistry
from .serializers import FederalMinistrySerializer


# Create your views here.

class FederalMinistriesList(generics.ListAPIView):
    serializer_class = FederalMinistrySerializer
    queryset = FederalMinistry.objects.all().order_by('full_name')
    ordering_fields = ('full_name', 'short_name', 'established', 'current_minister')
    search_fields = ('full_name', 'short_name', 'current_minister', 'permanent_secretary')


class FederalMinistryDetail(generics.RetrieveAPIView):
    serializer_class = FederalMinistrySerializer
    queryset = FederalMinistry.objects.all()
    lookup_field = 'full_name'
    lookup_url_kwarg = 'name'

