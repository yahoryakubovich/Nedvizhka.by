from django.db import models
from django.contrib.auth.models import User

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
    description = models.CharField(max_length=500)
    total_area = models.FloatField()
    address = models.CharField(max_length=80)
    facilities = models.CharField(max_length=500, blank=True)
    condition = models.CharField(choices=CONDITION, max_length=20)
    renovation = models.CharField(choices=RENOVATION, max_length=20)
    price = models.IntegerField(default="Договорная")
    photo = models.ImageField(blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    is_moderated = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Garage(Realty):
    quantity_parking_spaces = models.IntegerField()
    heating = models.CharField(choices=HEATING, max_length=20)
    condition = None

    def __str__(self):
        return self.title


class Parking(Realty):
    quantity_parking_spaces = models.IntegerField()
    condition = None

    def __str__(self):
        return self.title


class Warehouse(Realty):
    number_of_separate_premises = models.IntegerField()

    def __str__(self):
        return self.title


class Office(Realty):
    floor_number = models.IntegerField()

    def __str__(self):
        return self.title


class Trade(Realty):
    location = models.CharField(choices=LOCATION, max_length=20)

    def __str__(self):
        return self.title


class Industrial(Realty):
    number_of_separate_premises = models.IntegerField()

    def __str__(self):
        return self.title


class Flat(Realty):
    number_of_rooms = models.IntegerField()
    floor_number = models.IntegerField()
    living_area = models.FloatField()
    kitchen = models.FloatField()
    year_of_construction = models.IntegerField()

    def __str__(self):
        return self.title


class House(Realty):
    category = models.CharField(choices=CATEGORY, max_length=20)
    number_of_rooms = models.IntegerField()
    number_of_floors = models.IntegerField()
    living_area = models.FloatField()
    year_of_construction = models.IntegerField()

    def __str__(self):
        return self.title
