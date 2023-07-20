from django.urls import path
from .views import *

urlpatterns = [
    path('flat/', FlatListView.as_view(template_name="flat.html"), name='flat'),
    path('flat/<int:pk>', FlatDetailView.as_view(), name='flat'),
    path('flat/create/', FlatCreateView.as_view(), name="createflat"),
    path('house/', HouseListView.as_view(template_name="house.html"), name='house'),
    path('house/<int:pk>', HouseDetailView.as_view(), name='house'),
    path('house/create/', HouseCreateView.as_view(), name="createhouse"),
    path('garage/', GarageListView.as_view(template_name="garage.html"), name='garage'),
    path('garage/<int:pk>', GarageDetailView.as_view(), name='garage'),
    # path('garage/create/', GarageCreateView.as_view(), name="creategarage"),
    path('parking/', ParkingListView.as_view(template_name="parking.html"), name='parking'),
    path('parking/<int:pk>', ParkingDetailView.as_view(), name='parking'),
    # path('parking/create/', ParkingCreateView.as_view(), name="createparking"),
    path('warehouse/', WarehouseListView.as_view(template_name="warehouse.html"), name='warehouse'),
    # path('warehouse/<int:pk>', WarehouseDetailView.as_view(), name='warehouse'),
    # path('warehouse/create/', WarehouseCreateView.as_view(), name="createwarehouse"),
    path('office/', OfficeListView.as_view(template_name="office.html"), name='office'),
    # path('office/<int:pk>', OfficeDetailView.as_view(), name='office'),
    # path('office/create/', OfficeCreateView.as_view(), name="createoffice"),
    path('trade/', TradeListView.as_view(template_name="trade.html"), name='trade'),
    # path('trade/<int:pk>', TradeDetailView.as_view(), name='trade'),
    # path('trade/create/', TradeCreateView.as_view(), name="createtrade"),
    path('industrial/', IndustrialListView.as_view(template_name="industrial.html"), name='industrial'),
    # path('industrial/<int:pk>', IndustrialDetailView.as_view(), name='industrial'),
    # path('industrial/create/', IndustrialCreateView.as_view(), name="createindustrial")
]
