from django.urls import path
from .views import *

urlpatterns = [
    path('flat/', FlatListView.as_view(template_name="flat.html"), name='flat'),
    path('flat/<int:pk>', FlatDetailView.as_view(), name='flat'),
    path('flat/create/', FlatCreateView.as_view()),
    path('house/', HouseListView.as_view(template_name="house.html"), name='house'),
    path('house/<int:pk>', HouseDetailView.as_view(), name='house'),
    path('house/create/', HouseCreateView.as_view())
]