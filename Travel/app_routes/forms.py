from django import forms

from app_cities.models import CityModel
from .models import RouteModel


class RouteForm(forms.Form):
    departure_city = forms.ModelChoiceField(
        label='Город отправления',
        queryset=CityModel.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control js-example-basic-single'
        })
    )
    arrival_city = forms.ModelChoiceField(
        label='Город прибытия',
        queryset=CityModel.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control js-example-basic-single'
        })
    )
    travel_time = forms.IntegerField(
        label='Время в пути',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Время в пути'
        })
    )

    cities = forms.ModelMultipleChoiceField(
        label='Через города',
        queryset=CityModel.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control js-example-basic-multiple'
        })
    )

    class Meta:
        model = RouteModel
        fields = '__all__'
