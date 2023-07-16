from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import *
from django.urls import reverse_lazy


class SaleListView(ListView):
    model = [Garage, Parking, Warehouse, Office, Trade, Industrial, Flat, House]
    context_object_name = 'object_list'

    def get_queryset(self):
        queryset1 = Garage.objects.filter(is_moderated=True)
        queryset2 = Parking.objects.filter(is_moderated=True)
        queryset3 = Warehouse.objects.filter(is_moderated=True)
        queryset4 = Office.objects.filter(is_moderated=True)
        queryset5 = Trade.objects.filter(is_moderated=True)
        queryset6 = Industrial.objects.filter(is_moderated=True)
        queryset7 = Flat.objects.filter(is_moderated=True)
        queryset8 = House.objects.filter(is_moderated=True)

        return list(queryset1) + list(queryset2) + list(queryset3) + list(queryset4) + list(queryset5) + list(
            queryset6) + list(queryset7) + list(queryset8)


class FlatListView(ListView):
    model = Flat

    def get_queryset(self):
        return super().get_queryset().filter(is_moderated=True)


class HouseListView(ListView):
    model = House


class FlatDetailView(DetailView):
    model = Flat
    template_name = "flatdetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class HouseDetailView(DetailView):
    model = House
    template_name = "housedetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class FlatCreateView(LoginRequiredMixin, CreateView):
    model = Flat
    fields = '__all__'
    template_name = 'flatcreateview.html'
    login_url = 'login'
    success_url = reverse_lazy('flat')

    def form_valid(self, form):
        form.save()
        return super(FlatCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(FlatCreateView, self).form_valid(form)


class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    fields = '__all__'
    template_name = 'housecreateview.html'
    login_url = 'login'
    success_url = reverse_lazy('house')

    def form_valid(self, form):
        form.save()
        return super(HouseCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(HouseCreateView, self).form_valid(form)
