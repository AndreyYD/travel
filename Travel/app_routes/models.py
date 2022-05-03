from django.db import models

from app_cities.models import CityModel


class RouteModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Название маршрута')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    departure_city = models.ForeignKey(
        CityModel,
        on_delete=models.CASCADE,
        related_name='route_departure_city_set',
        verbose_name='Город отправления'
    )
    arrival_city = models.ForeignKey(
        'app_cities.CityModel',
        on_delete=models.CASCADE,
        related_name='route_arrival_city_set',
        verbose_name='Город прибытия'
    )
    trains = models.ManyToManyField('app_trains.TrainModel', verbose_name='Список поездов')

    def __str__(self):
        return f'Маршрут {self.name} из города {self.departure_city} в город {self.arrival_city}'

    class Meta:
        verbose_name = 'Маршрут'
        verbose_name_plural = 'Маршруты'
        ordering = ['travel_time']
