from django.core.exceptions import ValidationError
from django.db import models

from app_cities.models import CityModel


class TrainModel(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='Номер поезда')
    travel_time = models.PositiveSmallIntegerField(verbose_name='Время в пути')
    departure_city = models.ForeignKey(
        CityModel,
        on_delete=models.CASCADE,
        related_name='departure_city_set',
        verbose_name='Город отправления'
    )
    arrival_city = models.ForeignKey(
        'app_cities.CityModel',
        on_delete=models.CASCADE,
        related_name='arrival_city_set',
        verbose_name='Город прибытия'
    )

    def __str__(self):
        return f'Поезд №{self.name} из города {self.departure_city} в город {self.arrival_city}'

    class Meta:
        verbose_name = 'Поезд'
        verbose_name_plural = 'Поезда'
        ordering = ['travel_time']

    def clean(self):
        if self.departure_city == self.arrival_city:
            raise ValidationError('Изменить город прибытия')
        inquiry = TrainModel.objects.filter(
            departure_city=self.departure_city,
            arrival_city=self.arrival_city,
            travel_time=self.travel_time
        ).exclude(pk=self.pk)
        if inquiry.exists():
            raise ValidationError('Изменить время в пути')

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
