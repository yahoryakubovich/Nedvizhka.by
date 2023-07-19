from django.urls import path
from django.views.generic import *
from . import views

urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile'),
    path('edit_profile/', views.EditProfileView.as_view(), name='edit_profile'),
    path('create/', TemplateView.as_view(template_name="create.html"), name='create'),
]
