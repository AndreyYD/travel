from django.db import models
from django.urls import reverse

class CityModel(models.Model):
    name = models.CharField(max_length=30, unique=True, verbose_name='City')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'City'
        verbose_name_plural = 'Cities'
        ordering = ['name']

    def get_absolute_url(self):
        return reverse('city', kwargs={'pk': self.pk})
