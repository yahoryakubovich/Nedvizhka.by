from django.urls import path
from .views import *

urlpatterns = [
    path('flat/', FlatListView.as_view(template_name="flat.html"), name='flat'),
    path('flat/1-rooms-flats', FlatOneRoomListView.as_view(template_name="flat.html"), name='flat_one_room'),
    path('flat/2-rooms-flats', FlatTwoRoomListView.as_view(template_name="flat.html"), name='flat_two_room'),
    path('flat/3-rooms-flats', FlatThreeRoomListView.as_view(template_name="flat.html"), name='flat_three_room'),
    path('flat/4-rooms-flats', FlatFourRoomListView.as_view(template_name="flat.html"), name='flat_four_room'),
    path('flat/<int:pk>/', FlatDetailView.as_view(), name='flat'),
    path('flat/create/', FlatCreateView.as_view(), name="create_flat"),
    path('flat/<int:pk>/edit/', FlatUpdateView.as_view(), name='edit_flat'),
    path('flat/<int:pk>/delete/', FlatDeleteView.as_view(), name='delete_flat'),

    path('house/', HouseListView.as_view(template_name="house.html"), name='house'),
    path('house/<int:pk>/', HouseDetailView.as_view(), name='house'),
    path('house/create/', HouseCreateView.as_view(), name="create_house"),
    path('house/<int:pk>/edit/', HouseUpdateView.as_view(), name='edit_house'),
    path('house/<int:pk>/delete/', HouseDeleteView.as_view(), name='delete_house'),

    path('garage/', GarageListView.as_view(template_name="garage.html"), name='garage'),
    path('garage/<int:pk>/', GarageDetailView.as_view(), name='garage'),
    path('garage/create/', GarageCreateView.as_view(), name="create_garage"),
    path('garage/<int:pk>/edit/', GarageUpdateView.as_view(), name='edit_garage'),
    path('garage/<int:pk>/delete/', GarageDeleteView.as_view(), name='delete_garage'),

    path('parking/', ParkingListView.as_view(template_name="parking.html"), name='parking'),
    path('parking/<int:pk>/', ParkingDetailView.as_view(), name='parking'),
    path('parking/create/', ParkingCreateView.as_view(), name="create_parking"),
    path('parking/<int:pk>/edit/', ParkingUpdateView.as_view(), name='edit_parking'),
    path('parking/<int:pk>/delete/', ParkingDeleteView.as_view(), name='delete_parking'),

    path('warehouse/', WarehouseListView.as_view(template_name="warehouse.html"), name='warehouse'),
    path('warehouse/<int:pk>/', WarehouseDetailView.as_view(), name='warehouse'),
    path('warehouse/create/', WarehouseCreateView.as_view(), name="create_warehouse"),
    path('warehouse/<int:pk>/edit/', WarehouseUpdateView.as_view(), name='edit_warehouse'),
    path('warehouse/<int:pk>/delete/', WarehouseDeleteView.as_view(), name='delete_warehouse'),

    path('office/', OfficeListView.as_view(template_name="office.html"), name='office'),
    path('office/<int:pk>/', OfficeDetailView.as_view(), name='office'),
    path('office/create/', OfficeCreateView.as_view(), name="create_office"),
    path('office/<int:pk>/edit/', OfficeUpdateView.as_view(), name='edit_office'),
    path('office/<int:pk>/delete/', OfficeDeleteView.as_view(), name='delete_office'),

    path('trade/', TradeListView.as_view(template_name="trade.html"), name='trade'),
    path('trade/<int:pk>/', TradeDetailView.as_view(), name='trade'),
    path('trade/create/', TradeCreateView.as_view(), name="create_trade"),
    path('trade/<int:pk>/edit/', TradeUpdateView.as_view(), name='edit_trade'),
    path('trade/<int:pk>/delete/', TradeDeleteView.as_view(), name='delete_trade'),

    path('industrial/', IndustrialListView.as_view(template_name="industrial.html"), name='industrial'),
    path('industrial/<int:pk>/', IndustrialDetailView.as_view(), name='industrial'),
    path('industrial/create/', IndustrialCreateView.as_view(), name="create_industrial"),
    path('industrial/<int:pk>/edit/', IndustrialUpdateView.as_view(), name='edit_industrial'),
    path('industrial/<int:pk>/delete/', IndustrialDeleteView.as_view(), name='delete_industrial'),
]
