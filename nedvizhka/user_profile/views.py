from django.views.generic import TemplateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.views.generic import ListView
from sale.models import *
from .models import Profile
from .forms import ProfileForm

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = Profile.objects.get(user=self.request.user)
        flat_queryset = Flat.objects.filter(creator=self.request.user)
        house_queryset = House.objects.filter(creator=self.request.user)
        garage_queryset = Garage.objects.filter(creator=self.request.user)
        parking_queryset = Parking.objects.filter(creator=self.request.user)
        warehouse_queryset = Warehouse.objects.filter(creator=self.request.user)
        office_queryset = Office.objects.filter(creator=self.request.user)
        trade_queryset = Trade.objects.filter(creator=self.request.user)
        industrial_queryset = Industrial.objects.filter(creator=self.request.user)
        context['profile'] = profile
        context['flat_queryset'] = flat_queryset
        context['house_queryset'] = house_queryset
        context['garage_queryset'] = garage_queryset
        context['parking_queryset'] = parking_queryset
        context['warehouse_queryset'] = warehouse_queryset
        context['office_queryset'] = office_queryset
        context['trade_queryset'] = trade_queryset
        context['industrial_queryset'] = industrial_queryset
        return context


class EditProfileView(LoginRequiredMixin, UpdateView):
    model = Profile
    template_name = 'edit_profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile
