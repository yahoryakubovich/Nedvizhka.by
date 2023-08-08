from django import forms
from .models import *


class FlatForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Flat
        exclude = ['is_moderated', 'creator']
        labels = {
            'district': 'Район',
            'subway': 'Метро',
            'description': 'Описание',
            'facilities': 'Удобства',
            'total_area': 'Общая площадь',
            'kitchen': 'Площадь кухни',
            'address': 'Адрес',
            'condition': 'Состояние',
            'renovation': 'Ремонт',
            'price': 'Цена',
            'image': 'Фотография 1',
            'image_2': 'Фотография 2',
            'image_3': 'Фотография 3',
            'image_4': 'Фотография 4',
            'image_5': 'Фотография 5',
            'number_of_rooms': 'Количество комнат',
            'balcony': 'Балкон',
            'bathroom': 'Санузел',
            'floor_number': 'Этаж',
            'number_of_floors': 'Этажность дома',
            'living_area': 'Жилая площадь',
            'year_of_construction': 'Год постройки',
        }


class HouseForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = House
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
            'number_of_floors': 'Количество этажей',
            'living_area': 'Жилая площадь',
            'year_of_construction': 'Год постройки',
        }


class GarageForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Garage
        exclude = ['is_moderated', 'creator']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'total_area': 'Общая площадь',
            'address': 'Адрес',
            'facilities': 'Удобства',
            'price': 'Цена',
            'image': 'Фотография',
            'quantity_parking_spaces': 'Количество парковочный мест',
            'heating': 'Отопление'
        }


class ParkingForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Parking
        exclude = ['is_moderated', 'creator']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'total_area': 'Общая площадь',
            'address': 'Адрес',
            'facilities': 'Удобства',
            'price': 'Цена',
            'image': 'Фотография',
            'quantity_parking_spaces': 'Количество парковочных мест'
        }


class WarehouseForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Warehouse
        exclude = ['is_moderated', 'creator']
        labels = {
            'title': 'Заголовок',
            'total_area': 'Общая площадь',
            'address': 'Адрес',
            'price': 'Цена',
            'image': 'Фотография',
            'number_of_separate_premises': 'Количество раздельных помещений'
        }


class OfficeForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Office
        exclude = ['is_moderated', 'creator']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'facilities': 'Удобства',
            'total_area': 'Общая площадь',
            'address': 'Адрес',
            'condition': 'Состояние',
            'renovation': 'Ремонт',
            'price': 'Цена',
            'image': 'Фотография',
            'category': 'Категория',
            'floor_number': 'Этаж',
        }


class TradeForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Trade
        exclude = ['is_moderated', 'creator']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'facilities': 'Удобства',
            'total_area': 'Общая площадь',
            'address': 'Адрес',
            'condition': 'Состояние',
            'price': 'Цена',
            'image': 'Фотография',
            'location': 'Расположение'
        }


class IndustrialForm(forms.ModelForm):
    description = forms.CharField(label='Описание', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))
    facilities = forms.CharField(label='Удобства', widget=forms.Textarea(attrs={'cols': 40, 'rows': 10}))

    class Meta:
        model = Industrial
        exclude = ['is_moderated', 'creator']
        labels = {
            'title': 'Заголовок',
            'description': 'Описание',
            'facilities': 'Удобства',
            'total_area': 'Общая площадь',
            'address': 'Адрес',
            'price': 'Цена',
            'image': 'Фотография',
            'floor_number': 'Этаж',
            'number_of_separate_premises': 'Количество раздельных помещений'
        }
