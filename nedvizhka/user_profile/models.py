from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class Profile(models.Model):
    phone_regex = RegexValidator(
        regex=r'^\+375\d{9}$',
        message='Номер телефона должен быть в формате: "+375XXYYYYYYY", где XX - код оператора, а YYYYYYY - номер абонента.'
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=13, validators=[phone_regex])

    def __str__(self):
        return self.first_name
