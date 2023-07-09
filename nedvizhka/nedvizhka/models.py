from django.db import models


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
    CHOICES = (
        ("Y", "Yes"),
        ("N", "No")
    )
    quantity_parking_spaces = models.IntegerField()
    heating = models.Choices(CHOICES)


class Parking(Realty):
    quantity_parking_spaces = models.IntegerField()


class Commercial(Realty):
    class Meta:
        abstract = True


