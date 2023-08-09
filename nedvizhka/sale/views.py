from django.views.generic import *
from django.views.generic.edit import *
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .forms import *
from django.shortcuts import get_object_or_404
from django.db.models import Q


class FlatListView(ListView):
    model = Flat

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_moderated=True)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        subway = self.request.GET.get('subway')
        district = self.request.GET.get('district')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if subway:
            queryset = queryset.filter(subway=subway)

        if district:
            queryset = queryset.filter(district=district)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        context['subway'] = self.request.GET.get('subway')
        context['district'] = self.request.GET.get('district')
        return context


class FlatOneRoomListView(ListView):
    model = Flat

    def get_queryset(self):
        return super().get_queryset().filter(Q(is_moderated=True) & Q(number_of_rooms=1))


class FlatTwoRoomListView(ListView):
    model = Flat

    def get_queryset(self):
        return super().get_queryset().filter(Q(is_moderated=True) & Q(number_of_rooms=2))


class FlatThreeRoomListView(ListView):
    model = Flat

    def get_queryset(self):
        return super().get_queryset().filter(Q(is_moderated=True) & Q(number_of_rooms=3))


class FlatFourRoomListView(ListView):
    model = Flat

    def get_queryset(self):
        return super().get_queryset().filter(Q(is_moderated=True) & Q(number_of_rooms=4))


class HouseListView(ListView):
    model = House

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_moderated=True)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        subway = self.request.GET.get('subway')
        district = self.request.GET.get('district')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if subway:
            queryset = queryset.filter(subway=subway)

        if district:
            queryset = queryset.filter(district=district)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        context['subway'] = self.request.GET.get('subway')
        context['district'] = self.request.GET.get('district')
        return context


class GarageListView(ListView):
    model = Garage

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_moderated=True)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        subway = self.request.GET.get('subway')
        district = self.request.GET.get('district')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if subway:
            queryset = queryset.filter(subway=subway)

        if district:
            queryset = queryset.filter(district=district)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        context['subway'] = self.request.GET.get('subway')
        context['district'] = self.request.GET.get('district')
        return context


class ParkingListView(ListView):
    model = Parking

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_moderated=True)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        subway = self.request.GET.get('subway')
        district = self.request.GET.get('district')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if subway:
            queryset = queryset.filter(subway=subway)

        if district:
            queryset = queryset.filter(district=district)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        context['subway'] = self.request.GET.get('subway')
        context['district'] = self.request.GET.get('district')
        return context


class WarehouseListView(ListView):
    model = Warehouse

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_moderated=True)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        subway = self.request.GET.get('subway')
        district = self.request.GET.get('district')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if subway:
            queryset = queryset.filter(subway=subway)

        if district:
            queryset = queryset.filter(district=district)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        context['subway'] = self.request.GET.get('subway')
        context['district'] = self.request.GET.get('district')
        return context


class OfficeListView(ListView):
    model = Office

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_moderated=True)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        subway = self.request.GET.get('subway')
        district = self.request.GET.get('district')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if subway:
            queryset = queryset.filter(subway=subway)

        if district:
            queryset = queryset.filter(district=district)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        context['subway'] = self.request.GET.get('subway')
        context['district'] = self.request.GET.get('district')
        return context


class TradeListView(ListView):
    model = Trade

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_moderated=True)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        subway = self.request.GET.get('subway')
        district = self.request.GET.get('district')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if subway:
            queryset = queryset.filter(subway=subway)

        if district:
            queryset = queryset.filter(district=district)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        context['subway'] = self.request.GET.get('subway')
        context['district'] = self.request.GET.get('district')
        return context


class IndustrialListView(ListView):
    model = Industrial

    def get_queryset(self):
        queryset = super().get_queryset().filter(is_moderated=True)

        min_price = self.request.GET.get('min_price')
        max_price = self.request.GET.get('max_price')
        subway = self.request.GET.get('subway')
        district = self.request.GET.get('district')

        if min_price and max_price:
            queryset = queryset.filter(price__gte=min_price, price__lte=max_price)
        elif min_price:
            queryset = queryset.filter(price__gte=min_price)
        elif max_price:
            queryset = queryset.filter(price__lte=max_price)

        if subway:
            queryset = queryset.filter(subway=subway)

        if district:
            queryset = queryset.filter(district=district)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['min_price'] = self.request.GET.get('min_price')
        context['max_price'] = self.request.GET.get('max_price')
        context['subway'] = self.request.GET.get('subway')
        context['district'] = self.request.GET.get('district')
        return context

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


class GarageDetailView(DetailView):
    model = Garage
    template_name = "garagedetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class ParkingDetailView(DetailView):
    model = Parking
    template_name = "parkingdetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class WarehouseDetailView(DetailView):
    model = Warehouse
    template_name = "warehousedetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class OfficeDetailView(DetailView):
    model = Office
    template_name = "officedetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class TradeDetailView(DetailView):
    model = Trade
    template_name = "tradedetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class IndustrialDetailView(DetailView):
    model = Industrial
    template_name = "industrialdetailview.html"

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class FlatCreateView(LoginRequiredMixin, CreateView):
    model = Flat
    form_class = FlatForm
    template_name = 'flatcreateview.html'
    login_url = 'account_login'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    form_class = HouseForm
    template_name = 'housecreateview.html'
    login_url = 'account_login'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class GarageCreateView(LoginRequiredMixin, CreateView):
    model = Garage
    form_class = GarageForm
    template_name = 'garagecreateview.html'
    login_url = 'account_login'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class ParkingCreateView(LoginRequiredMixin, CreateView):
    model = Parking
    form_class = ParkingForm
    template_name = 'parkingcreateview.html'
    login_url = 'account_login'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class WarehouseCreateView(LoginRequiredMixin, CreateView):
    model = Warehouse
    form_class = WarehouseForm
    template_name = 'warehousecreateview.html'
    login_url = 'account_login'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class OfficeCreateView(LoginRequiredMixin, CreateView):
    model = Office
    form_class = OfficeForm
    template_name = 'officecreateview.html'
    login_url = 'account_login'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TradeCreateView(LoginRequiredMixin, CreateView):
    model = Trade
    form_class = TradeForm
    template_name = 'tradecreateview.html'
    login_url = 'account_login'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class IndustrialCreateView(LoginRequiredMixin, CreateView):
    model = Industrial
    form_class = IndustrialForm
    template_name = 'industrialcreateview.html'
    login_url = 'account_login'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class FlatUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit.html'
    form_class = FlatForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return get_object_or_404(Flat, pk=self.kwargs['pk'], creator=self.request.user)

    def test_func(self):
        flat = self.get_object()
        return flat.creator == self.request.user

    def form_valid(self, form):
        form.instance.is_moderated = False
        return super().form_valid(form)


class HouseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit.html'
    form_class = HouseForm

    def get_object(self, queryset=None):
        return get_object_or_404(House, pk=self.kwargs['pk'], creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')

    def test_func(self):
        flat = self.get_object()
        return flat.creator == self.request.user

    def form_valid(self, form):
        form.instance.is_moderated = False
        return super().form_valid(form)


class GarageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit.html'
    form_class = GarageForm

    def get_object(self, queryset=None):
        return get_object_or_404(Garage, pk=self.kwargs['pk'], creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')

    def test_func(self):
        flat = self.get_object()
        return flat.creator == self.request.user

    def form_valid(self, form):
        form.instance.is_moderated = False
        return super().form_valid(form)


class ParkingUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit.html'
    form_class = ParkingForm

    def get_object(self, queryset=None):
        return get_object_or_404(Parking, pk=self.kwargs['pk'], creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')

    def test_func(self):
        flat = self.get_object()
        return flat.creator == self.request.user

    def form_valid(self, form):
        form.instance.is_moderated = False
        return super().form_valid(form)


class WarehouseUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit.html'
    form_class = WarehouseForm

    def get_object(self, queryset=None):
        return get_object_or_404(Warehouse, pk=self.kwargs['pk'], creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')

    def test_func(self):
        flat = self.get_object()
        return flat.creator == self.request.user

    def form_valid(self, form):
        form.instance.is_moderated = False
        return super().form_valid(form)


class OfficeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit.html'
    form_class = OfficeForm

    def get_object(self, queryset=None):
        return get_object_or_404(Office, pk=self.kwargs['pk'], creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')

    def test_func(self):
        flat = self.get_object()
        return flat.creator == self.request.user

    def form_valid(self, form):
        form.instance.is_moderated = False
        return super().form_valid(form)


class TradeUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit.html'
    form_class = TradeForm

    def get_object(self, queryset=None):
        return get_object_or_404(Trade, pk=self.kwargs['pk'], creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')

    def test_func(self):
        flat = self.get_object()
        return flat.creator == self.request.user

    def form_valid(self, form):
        form.instance.is_moderated = False
        return super().form_valid(form)


class IndustrialUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = 'edit.html'
    form_class = IndustrialForm

    def get_object(self, queryset=None):
        return get_object_or_404(Industrial, pk=self.kwargs['pk'], creator=self.request.user)

    def get_success_url(self):
        return reverse_lazy('profile')

    def test_func(self):
        flat = self.get_object()
        return flat.creator == self.request.user

    def form_valid(self, form):
        form.instance.is_moderated = False
        return super().form_valid(form)


class FlatDeleteView(LoginRequiredMixin, DeleteView):
    model = Flat
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class HouseDeleteView(LoginRequiredMixin, DeleteView):
    model = House
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class GarageDeleteView(LoginRequiredMixin, DeleteView):
    model = Garage
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class ParkingDeleteView(LoginRequiredMixin, DeleteView):
    model = Parking
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class WarehouseDeleteView(LoginRequiredMixin, DeleteView):
    model = Warehouse
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class OfficeDeleteView(LoginRequiredMixin, DeleteView):
    model = Office
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class TradeDeleteView(LoginRequiredMixin, DeleteView):
    model = Trade
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)


class IndustrialDeleteView(LoginRequiredMixin, DeleteView):
    model = Industrial
    template_name = 'delete.html'
    success_url = reverse_lazy('profile')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(creator=self.request.user)
