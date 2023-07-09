from django.db import models


# CATEGORY = [
#     ("r", "residential"),
#     ("n", "non-residential"),
#     ("c", "commercial")
# ]


class Realty(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100)
    square = models.FloatField()
    address = models.CharField(max_length=30)
    facilities = models.CharField(max_length=50)
    price = models.IntegerField()
    photo = models.ImageField(blank=True)

    class Meta:
        abstract = True


class Garage(Realty):
    CHOICES = [
        ("y", "yes"),
        ("n", "no")
    ]
    quantity_parking_spaces = models.IntegerField()
    heating = models.Choices(CHOICES)


class Parking(Realty):
    quantity_parking_spaces = models.IntegerField()


class Warehouse(Realty):
    pass


class Office(Realty):
    pass


class Trade(Realty):
    pass


class Industrial(Realty):
    pass


class Flat(Realty):
    pass


class House(Realty):
    CATEGORY = [
        ("д", "дом"),
        ("к", "коттедж"),
        ("у", "усадьба")
    ]
