from django.views.generic import *
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import *
from .forms import *


class FlatListView(ListView):
    model = Flat
    paginate_by = 20

    def get_queryset(self):
        return super().get_queryset().filter(is_moderated=True)


class HouseListView(ListView):
    model = House

    def get_queryset(self):
        return super().get_queryset().filter(is_moderated=True)


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


# class FlatCreateView(LoginRequiredMixin, CreateView):
#     model = Flat
#     fields = '__all__'
#     template_name = 'flatcreateview.html'
#     login_url = ('account_login')
#     success_url = reverse_lazy('flat')
#
#     def form_valid(self, form):
#         form.save()
#         return super(FlatCreateView, self).form_valid(form)
#
#     def form_invalid(self, form):
#         return super(FlatCreateView, self).form_valid(form)

class FlatCreateView(LoginRequiredMixin, CreateView):
    model = Flat
    form_class = FlatForm
    template_name = 'flatcreateview.html'
    login_url = ('account_login')
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class HouseCreateView(LoginRequiredMixin, CreateView):
    model = House
    fields = '__all__'
    template_name = 'housecreateview.html'
    login_url = ('account_login')
    success_url = reverse_lazy('house')

    def form_valid(self, form):
        form.save()
        return super(HouseCreateView, self).form_valid(form)

    def form_invalid(self, form):
        return super(HouseCreateView, self).form_valid(form)
