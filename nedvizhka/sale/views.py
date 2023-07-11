from django.shortcuts import render
from django.views.generic import *
from .models import *


class FlatListView(ListView):
    model = Flat

