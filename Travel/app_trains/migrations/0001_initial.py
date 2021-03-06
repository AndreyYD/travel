# Generated by Django 3.2 on 2022-03-21 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_cities', '0003_alter_citymodel_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='TrainModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')),
                ('travel_time', models.PositiveSmallIntegerField(verbose_name='Время в пути')),
                ('arrival_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arrival_city_set', to='app_cities.citymodel', verbose_name='Город прибытия')),
                ('departure_city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departure_city_set', to='app_cities.citymodel', verbose_name='Город отправления')),
            ],
            options={
                'verbose_name': 'Поезд',
                'verbose_name_plural': 'Поезда',
                'ordering': ['travel_time'],
            },
        ),
    ]
