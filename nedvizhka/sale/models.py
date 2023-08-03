from django.db import models
from django.core.validators import MinValueValidator
from django.contrib.auth.models import User
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
    ("Y", "есть"),
    ("N", "отсутствует")
]
LOCATION = [
    ("S", "отдельное здание"),
    ("M", "в торговом центре")
]
CATEGORY = [
    ("H", "дом"),
    ("C", "коттедж"),
    ("M", "усадьба")
]


class Realty(models.Model):
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    description = models.CharField(max_length=4000)
    total_area = models.FloatField()
    facilities = models.CharField(max_length=2000, blank=True)
    condition = models.CharField(choices=CONDITION, max_length=20)
    renovation = models.CharField(choices=RENOVATION, max_length=20)
    price = models.PositiveIntegerField()
    image = models.ImageField(null=True, blank=True, upload_to="images")
    image2 = models.ImageField(null=True, blank=True, upload_to="images")
    image3 = models.ImageField(null=True, blank=True, upload_to="images")
    image4 = models.ImageField(null=True, blank=True, upload_to="images")
    image5 = models.ImageField(null=True, blank=True, upload_to="images")
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

    def __str__(self):
        return self.title


class Parking(Realty):
    quantity_parking_spaces = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])  # Валидатор для количества парковочных мест
    condition = None
    renovation = None

    def __str__(self):
        return self.title


class Warehouse(Realty):
    number_of_separate_premises = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])  # Валидатор для количества отдельных помещений
    condition = None
    renovation = None

    def __str__(self):
        return self.title


class Office(Realty):
    floor_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для номера этажа

    def __str__(self):
        return self.title


class Trade(Realty):
    location = models.CharField(choices=LOCATION, max_length=20)
    renovation = None

    def __str__(self):
        return self.title


class Industrial(Realty):
    number_of_separate_premises = models.PositiveIntegerField(
        validators=[MinValueValidator(1)])  # Валидатор для количества отдельных помещений
    condition = None
    renovation = None

    def __str__(self):
        return self.title


class Flat(Realty):
    number_of_rooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для количества комнат
    floor_number = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для номера этажа
    living_area = models.FloatField(validators=[MinValueValidator(0)])  # Валидатор для жилой площади
    kitchen = models.FloatField(validators=[MinValueValidator(0)])  # Валидатор для площади кухни
    year_of_construction = models.PositiveIntegerField(validators=[validate_year_of_construction])

    def __str__(self):
        return self.title


class House(Realty):
    category = models.CharField(choices=CATEGORY, max_length=20)
    number_of_rooms = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для количества комнат
    number_of_floors = models.PositiveIntegerField(validators=[MinValueValidator(1)])  # Валидатор для количества этажей
    living_area = models.FloatField(validators=[MinValueValidator(0)])  # Валидатор для жилой площади
    year_of_construction = models.PositiveIntegerField(validators=[validate_year_of_construction])

    def __str__(self):
        return self.title
