from rest_framework import generics
from sale.models import Flat
from api.serializers import FlatSerializer

class FlatListCreateView(generics.ListCreateAPIView):
    queryset = Flat.objects.filter(is_moderated=True)
    serializer_class = FlatSerializer

class FlatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.filter(is_moderated=True)
    serializer_class = FlatSerializer