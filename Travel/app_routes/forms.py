from django import forms

from app_cities.models import CityModel
from .models import RouteModel
from app_trains.models import TrainModel


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

class RouteModelForm(forms.ModelForm):
    name = forms.CharField(
        label='Название маршрута',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите название маршрута',
        })
    )
    departure_city = forms.ModelChoiceField(
        queryset=CityModel.objects.all(),
        widget=forms.HiddenInput(),
    )
    arrival_city = forms.ModelChoiceField(
        queryset=CityModel.objects.all(),
        widget=forms.HiddenInput(),
    )
    travel_time = forms.IntegerField(
        widget=forms.HiddenInput()
    )

    trains = forms.ModelMultipleChoiceField(
        queryset=TrainModel.objects.all(),
        required=False,
        widget=forms.SelectMultiple(attrs={
            'class': 'form-control d-none'
        })
    )

    class Meta:
        model = RouteModel
        fields = '__all__'
