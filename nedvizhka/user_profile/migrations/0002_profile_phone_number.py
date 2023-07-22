# Generated by Django 4.2.3 on 2023-07-22 22:38

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(default=0, max_length=13, validators=[django.core.validators.RegexValidator(message='Номер телефона должен быть в формате: "+375XXYYYYYYY", где XX - код оператора, а YYYYYYY - номер абонента.', regex='^\\+375\\d{9}$')]),
            preserve_default=False,
        ),
    ]
