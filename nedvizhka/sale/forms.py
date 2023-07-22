from django import forms
from .models import *


class FlatForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['description'].widget.attrs.update(size='40')

    class Meta:
        model = Flat
        exclude = ['is_moderated', 'creator']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'facilities': 'Удобства',
            'total_area': 'Общая площадь',
            'kitchen': 'Площадь кухни',
            'address': 'Адрес',
            'condition': 'Состояние',
            'renovation': 'Ремонт',
            'price': 'Цена',
            'image': 'Фотография',
            'category': 'Категория',
            'number_of_rooms': 'Количество комнат',
            'floor_number': 'Этаж',
            'living_area': 'Жилая площадь',
            'year_of_construction': 'Год постройки',
        }
