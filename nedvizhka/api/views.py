from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from sale.models import Flat, House
from api.serializers import FlatSerializer, HouseSerializer



class FlatListCreateView(generics.ListCreateAPIView):
    queryset = Flat.objects.filter(is_moderated=True)
    serializer_class = FlatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class FlatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.filter(is_moderated=True)
    serializer_class = FlatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class HouseListCreateView(generics.ListCreateAPIView):
    queryset = House.objects.filter(is_moderated=True)
    serializer_class = HouseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]


class HouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter(is_moderated=True)
    serializer_class = HouseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]