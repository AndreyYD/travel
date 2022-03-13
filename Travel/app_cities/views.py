from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import CityModel


def list_cities_view(request, pk=None):
    cities = CityModel.objects.all()
    context = {
        'cities': cities,
    }
    return render(request, 'cities/list_cities.html', context)

class CityDetailView(DetailView):
    queryset = CityModel.objects.all()
    template_name = 'cities/city.html'
