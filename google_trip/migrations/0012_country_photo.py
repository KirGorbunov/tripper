# Generated by Django 4.1.3 on 2022-12-08 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_trip', '0011_alter_hotels_type_of_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='photo',
            field=models.ImageField(null=True, upload_to='countries_images', verbose_name='Изображение'),
        ),
    ]
