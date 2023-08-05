# Generated by Django 4.2.3 on 2023-08-04 22:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sale', '0011_rename_image2_flat_image_2_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='bathroom',
            field=models.CharField(choices=[('S', 'Раздельный'), ('C', 'Совмещенный'), ('2', 'Два'), ('3', 'Три')], default='2', max_length=20),
            preserve_default=False,
        ),
    ]