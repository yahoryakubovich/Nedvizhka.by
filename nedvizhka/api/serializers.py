from rest_framework import serializers
from sale.models import Flat, House


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
