from django.urls import path
from .views import FlatListCreateView, FlatRetrieveUpdateDestroyView

urlpatterns = [
    path('flat/', FlatListCreateView.as_view(), name='flat-list-create'),
    path('flat/<int:pk>/', FlatRetrieveUpdateDestroyView.as_view(), name='flat-retrieve-update-destroy'),
]