from rest_framework import serializers
from sale.models import *


class FlatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flat
        fields = ['id', 'title', 'description', 'total_area', 'address', 'facilities', 'condition', 'renovation',
                  'price', 'number_of_rooms', 'image', 'floor_number', 'living_area', 'kitchen', 'year_of_construction']


class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = ['id', 'title', 'description', 'total_area', 'address', 'facilities', 'condition', 'renovation',
                  'price', 'category', 'image', 'number_of_rooms', 'number_of_floors', 'living_area',
                  'year_of_construction']


class GarageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Garage
        fields = ['id', 'title', 'description', 'total_area', 'address', 'facilities', ' quantity_parking_spaces',
                  'heating', 'price', 'image']


class ParkingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parking
        fields = ['id', 'title', 'description', 'total_area', 'address', 'facilities', ' quantity_parking_spaces',
                  'price', 'image']


class WarehouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Warehouse
        fields = ['id', 'title', 'description', 'total_area', 'address', 'facilities',
                  'number_of_separate_premises', 'price', 'image']


class OfficeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Office
        fields = ['id', 'title', 'description', 'total_area', 'address', 'facilities',
                  'condition', 'floor_number', 'price', 'image']


class TradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trade
        fields = ['id', 'title', 'description', 'total_area', 'address', 'facilities',
                  'location', 'price', 'image']


class IndustrialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Industrial
        fields = ['id', 'title', 'description', 'total_area', 'address', 'facilities',
                  'number_of_separate_premises',
                  'price', 'image']
