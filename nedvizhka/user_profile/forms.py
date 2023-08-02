from django import forms
from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'phone_number']
        labels = {
        'first_name': 'Имя',
        'last_name': 'Фамилия',
        'phone_number': 'Номер телефона'
        }
