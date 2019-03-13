from django.shortcuts import render
from rest_framework import generics
from .models import University
from .serializers import UniversitiesSerializers

# Create your views here.

class UniversitiesList(generics.ListAPIView):
    serializer_class = UniversitiesSerializers
    queryset = University.objects.all().order_by('nick_name')
    # filter_backends = (DjangoFilterBackend, )
    filter_fields = ('type', 'established', 'state',)
    ordering_fields = ('full_name', 'nick_name', 'established', 'state')
    search_fields = ('full_name', 'nick_name',)

class UniversityDetail(generics.RetrieveAPIView):
    serializer_class = UniversitiesSerializers
    queryset = University.objects.all()
    lookup_field = 'nick_name'
    lookup_url_kwarg = 'nick'