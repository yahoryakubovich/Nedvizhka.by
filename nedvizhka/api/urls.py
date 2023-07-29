from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import *

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('flat/', FlatListCreateView.as_view(), name='flat-list-create'),
    path('flat/<int:pk>/', FlatRetrieveUpdateDestroyView.as_view(), name='flat-retrieve-update-destroy'),
    path('house/', HouseListCreateView.as_view(), name='house-list-create'),
    path('house/<int:pk>/', HouseRetrieveUpdateDestroyView.as_view(), name='house-retrieve-update-destroy'),
    path('garage/', GarageListCreateView.as_view(), name='garage-list-create'),
    path('garage/<int:pk>/', GarageRetrieveUpdateDestroyView.as_view(), name='garage-retrieve-update-destroy'),
    path('parking/', ParkingListCreateView.as_view(), name='parking-list-create'),
    path('parking/<int:pk>/', ParkingRetrieveUpdateDestroyView.as_view(), name='parking-retrieve-update-destroy'),
    path('warehouse/', WarehouseListCreateView.as_view(), name='warehouse-list-create'),
    path('warehouse/<int:pk>/', WarehouseRetrieveUpdateDestroyView.as_view(), name='warehouse-retrieve-update-destroy'),
    path('office/', OfficeListCreateView.as_view(), name='office-list-create'),
    path('office/<int:pk>/', OfficeRetrieveUpdateDestroyView.as_view(), name='office-retrieve-update-destroy'),
    path('trade/', TradeListCreateView.as_view(), name='trade-list-create'),
    path('trade/<int:pk>/', TradeRetrieveUpdateDestroyView.as_view(), name='trade-retrieve-update-destroy'),
    path('industrial/', IndustrialListCreateView.as_view(), name='industrial-list-create'),
    path('industrial/<int:pk>/', IndustrialRetrieveUpdateDestroyView.as_view(),
         name='industrial-retrieve-update-destroy'),
]
