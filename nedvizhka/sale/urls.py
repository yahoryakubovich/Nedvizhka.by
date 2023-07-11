from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('flat/', FlatListView.as_view(template_name="flat.html"), name='flat'),
]
