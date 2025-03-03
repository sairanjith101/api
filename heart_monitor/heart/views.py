from rest_framework import generics
from .models import *
from .serializers import *

class HeartRateListCreateView(generics.ListCreateAPIView):
    queryset = HeartRate.objects.all()
    serializer_class = HeartRateSerializer

class HeartRateRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HeartRate.objects.all()
    serializer_class = HeartRateSerializer