from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone


def validate_year_of_construction(value):
    current_year = timezone.now().year
    if value < 1800 or value > current_year:
        raise ValidationError("Неправильный год постройки. Укажите год между 1800 и текущим годом.")


RENOVATION = [
    ("N", "без отделки"),
    ("Y", "с отделкой"),
    ("C", "косметический"),
    ("R", "евроремонт"),
    ("D", "дизайнерский")
]

CONDITION = [
    ("N", "новостройка"),
    ("S", "вторичка")
]

HEATING = [
    ('Gas', 'Газовое'),
    ('Central', 'Центральное'),
    ('Electric', 'Электрическое'),
    ('Stove', 'Печное'),
    ('No', 'Отсутствует'),
]

WATER = [
    ('Seasonal', 'Сезонная'),
    ('Well', 'Колодец'),
    ('Central', 'Центральная'),
    ('No', 'Отсутствует'),
]

SEWERAGE = [
    ('Central', 'Центральная'),
    ('Pit latrine', 'Выгребная яма'),
    ('Septic tank', 'Септик'),
    ('Biological treatment', 'Биологическая очистка'),
    ('Outdoor WC', 'С/у на улице'),
    ('No', 'Отсутствует'),
]

CATEGORY = [
    ("H", "дом"),
    ("C", "коттедж"),
    ("M", "усадьба")
]

BATHROOM = [
    ("S", "Раздельный"),
    ("C", "Совмещенный"),
    ("2", "Два"),
    ("3", "Три")
]

BALCONY = [
    ('Y', 'Есть'),
    ('N', 'Нет'),
    ('Loggia', 'Лоджия'),
    ('2', 'Два')
]

DISTRICT = [
    ("Z", "Заводской"),
    ("L", "Ленинский"),
    ("M", "Московский"),
    ("O", "Октябрьский"),
    ("P", "Партизанский"),
    ("PM", "Первомайский"),
    ("S", "Советсткий"),
    ("F", "Фрунзенский")
]

SUBWAY = [
    ("110", "Малиновка"),
    ("111", "Петровщина"),
    ("112", "Михалово"),
    ("113", "Грушевка"),
    ("114", "Институт культуры"),
    ("115", "Площадь Ленина"),
    ("116", "Октябрьская"),
    ("117", "Площадь Победы"),
    ("118", "Площадь Якуба Коласа"),
    ("119", "Академия Наук"),
    ("120", "Парк Челюскинцев"),
    ("121", "Московская"),
    ("122", "Восток"),
    ("123", "Борисовский тракт"),
    ("124", "Уручье"),
    ("210", "Каменная горка"),
    ("211", "Кунцевщина"),
    ("212", "Спортивная"),
    ("213", "Пушкинская"),
    ("214", "Молодёжная"),
    ("215", "Фрунзенская"),
    ("216", "Немига"),
    ("217", "Купаловская"),
    ("218", "Первомайская"),
    ("219", "Пролетарская"),
    ("220", "Тракторный завод"),
    ("221", "Партизанская"),
    ("222", "Автозаводская"),
    ("223", "Могилёвская"),
    ("313", "Ковальская Слобода"),
    ("314", "Вокзальная"),
    ("315", "Площадь Франтишка Богушевича"),
    ("316", "Юбилейная площадь"),

]

LOCATION = [
    ("S", "отдельное здание"),
    ("M", "в торговом центре")
]


class Realty(models.Model):
    address = models.CharField(max_length=100)
    district = models.CharField(choices=DISTRICT, max_length=40, blank=True)
    subway = models.CharField(choices=SUBWAY, max_length=50, blank=True)
    description = models.CharField(max_length=4000)
    total_area = models.FloatField(validators=[MinValueValidator(10)])
    facilities = models.CharField(max_length=2000, blank=True)
    condition = models.CharField(choices=CONDITION, max_length=20)
    renovation = models.CharField(choices=RENOVATION, max_length=20)
    price = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    image = models.ImageField(null=True, blank=True, upload_to="images")
    image_2 = models.ImageField(null=True, blank=True, upload_to="images")
    image_3 = models.ImageField(null=True, blank=True, upload_to="images")
    image_4 = models.ImageField(null=True, blank=True, upload_to="images")
    image_5 = models.ImageField(null=True, blank=True, upload_to="images")
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    is_moderated = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Garage(Realty):
    quantity_parking_spaces = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])  # Валидатор для количества парковочных мест
    heating = models.CharField(choices=HEATING, max_length=20)
    condition = None
    renovation = None



class Parking(Realty):
    quantity_parking_spaces = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])  # Валидатор для количества парковочных мест
    condition = None
    renovation = None



class Warehouse(Realty):
    number_of_separate_premises = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])  # Валидатор для количества отдельных помещений
    condition = None
    renovation = None



class Office(Realty):
    floor_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для номера этажа


class Trade(Realty):
    location = models.CharField(choices=LOCATION, max_length=20)
    renovation = None



class Industrial(Realty):
    number_of_separate_premises = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])  # Валидатор для количества отдельных помещений
    condition = None
    renovation = None


class Flat(Realty):
    number_of_rooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для количества комнат
    balcony = models.CharField(max_length=20, choices=BALCONY)
    bathroom = models.CharField(max_length=20, choices=BATHROOM)
    floor_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для номера этажа
    number_of_floors = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    living_area = models.FloatField(validators=[MinValueValidator(0)])  # Валидатор для жилой площади
    kitchen = models.FloatField(validators=[MinValueValidator(0)], blank=True)  # Валидатор для площади кухни
    year_of_construction = models.PositiveIntegerField(validators=[validate_year_of_construction])


class House(Realty):
    yard_area = models.FloatField()
    category = models.CharField(max_length=20, choices=CATEGORY)
    heating = models.CharField(max_length=20, choices=HEATING)
    water = models.CharField(max_length=20, choices=WATER)
    sewerage = models.CharField(max_length=20, choices=SEWERAGE)
    number_of_rooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для количества комнат
    number_of_floors = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для количества этажей
    living_area = models.FloatField(validators=[MinValueValidator(0)])  # Валидатор для жилой площади
    year_of_construction = models.PositiveIntegerField(validators=[validate_year_of_construction])

