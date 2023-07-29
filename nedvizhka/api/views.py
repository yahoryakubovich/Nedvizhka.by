from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from sale.models import *
from api.serializers import *


class FlatListCreateView(generics.ListCreateAPIView):
    queryset = Flat.objects.filter(is_moderated=True)
    serializer_class = FlatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class FlatRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Flat.objects.filter(is_moderated=True)
    serializer_class = FlatSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class HouseListCreateView(generics.ListCreateAPIView):
    queryset = House.objects.filter(is_moderated=True)
    serializer_class = HouseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class HouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = House.objects.filter(is_moderated=True)
    serializer_class = HouseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GarageListCreateView(generics.ListCreateAPIView):
    queryset = Garage.objects.filter(is_moderated=True)
    serializer_class = GarageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class GarageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Garage.objects.filter(is_moderated=True)
    serializer_class = GarageSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ParkingListCreateView(generics.ListCreateAPIView):
    queryset = Parking.objects.filter(is_moderated=True)
    serializer_class = ParkingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class ParkingRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Parking.objects.filter(is_moderated=True)
    serializer_class = ParkingSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class WarehouseListCreateView(generics.ListCreateAPIView):
    queryset = Warehouse.objects.filter(is_moderated=True)
    serializer_class = WarehouseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class WarehouseRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Warehouse.objects.filter(is_moderated=True)
    serializer_class = WarehouseSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class OfficeListCreateView(generics.ListCreateAPIView):
    queryset = Office.objects.filter(is_moderated=True)
    serializer_class = OfficeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class OfficeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Office.objects.filter(is_moderated=True)
    serializer_class = OfficeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TradeListCreateView(generics.ListCreateAPIView):
    queryset = Trade.objects.filter(is_moderated=True)
    serializer_class = TradeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class TradeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Trade.objects.filter(is_moderated=True)
    serializer_class = TradeSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class IndustrialListCreateView(generics.ListCreateAPIView):
    queryset = Industrial.objects.filter(is_moderated=True)
    serializer_class = IndustrialSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class IndustrialRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Industrial.objects.filter(is_moderated=True)
    serializer_class = IndustrialSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)
