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
]