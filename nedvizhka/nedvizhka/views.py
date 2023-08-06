from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from sale.models import Realty, Garage, Parking, Warehouse, Office, Trade, Industrial, Flat, House


class NedvizhkaView(TemplateView):
    template_name = 'nedvizhka.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flat_queryset = Flat.objects.filter(is_moderated=True)
        house_queryset = House.objects.filter(is_moderated=True)
        garage_queryset = Garage.objects.filter(is_moderated=True)
        parking_queryset = Parking.objects.filter(is_moderated=True)
        warehouse_queryset = Warehouse.objects.filter(is_moderated=True)
        office_queryset = Office.objects.filter(is_moderated=True)
        trade_queryset = Trade.objects.filter(is_moderated=True)
        industrial_queryset = Industrial.objects.filter(is_moderated=True)
        context['flat_queryset'] = flat_queryset
        context['house_queryset'] = house_queryset
        context['garage_queryset'] = garage_queryset
        context['parking_queryset'] = parking_queryset
        context['warehouse_queryset'] = warehouse_queryset
        context['office_queryset'] = office_queryset
        context['trade_queryset'] = trade_queryset
        context['industrial_queryset'] = industrial_queryset
        return context
