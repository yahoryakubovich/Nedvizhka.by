from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from sale.models import Realty, Garage, Parking, Warehouse, Office, Trade, Industrial, Flat, House


def real_estate_search(request):
    if request.method == 'GET':
        search_query = request.GET.get('search')
        results = []

        if search_query:
            models_to_search = [Garage, Parking, Warehouse, Office, Trade, Industrial, Flat, House]

            for model in models_to_search:
                objects = model.objects.filter(title__icontains=search_query)
                results.extend(objects)

        return render(request, 'real_estate_search.html', {'results': results})

    return render(request, 'real_estate_search.html')

class NedvizhkaView(LoginRequiredMixin, TemplateView):
    template_name = 'nedvizhka.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        flat_queryset = Flat.objects.filter(creator=self.request.user)
        house_queryset = House.objects.filter(creator=self.request.user)
        garage_queryset = Garage.objects.filter(creator=self.request.user)
        parking_queryset = Parking.objects.filter(creator=self.request.user)
        warehouse_queryset = Warehouse.objects.filter(creator=self.request.user)
        office_queryset = Office.objects.filter(creator=self.request.user)
        trade_queryset = Trade.objects.filter(creator=self.request.user)
        industrial_queryset = Industrial.objects.filter(creator=self.request.user)
        context['flat_queryset'] = flat_queryset
        context['house_queryset'] = house_queryset
        context['garage_queryset'] = garage_queryset
        context['parking_queryset'] = parking_queryset
        context['warehouse_queryset'] = warehouse_queryset
        context['office_queryset'] = office_queryset
        context['trade_queryset'] = trade_queryset
        context['industrial_queryset'] = industrial_queryset
        return context
