# Generated by Django 4.1.3 on 2022-12-15 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('google_trip', '0016_alter_hotels_name_alter_restaurant_name_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Hotels',
            new_name='Hotel',
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='country',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='county',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='region',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='state',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='town',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Город'),
        ),
        migrations.AlterField(
            model_name='village',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Город'),
        ),
    ]
