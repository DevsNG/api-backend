from rest_framework import generics
from .models import State
from .serializers import StateSerializer


# Create your views here.

class StatesList(generics.ListAPIView):
    serializer_class = StateSerializer
    queryset = State.objects.all().order_by('name')
    filter_fields = ('created_on', 'created_from', 'geopolitical_zone', 'no_of_local_governments', 'governor', 'vice_governor')
    ordering_fields = ('name', 'created_on', 'capital', 'geopolitical_zone',)
    search_fields = ('name', 'landmarks', 'capital',)


class StateDetail(generics.RetrieveAPIView):
    serializer_class = StateSerializer
    queryset = State.objects.all()
    lookup_field = 'name'
    #lookup_url_kwarg = 'name'


