# Generated by Django 4.1.3 on 2022-12-11 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_trip', '0015_alter_hotels_name_alter_restaurant_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotels',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='touristattraction',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
    ]