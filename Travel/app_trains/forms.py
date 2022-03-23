from django import forms

from app_cities.models import CityModel
from .models import TrainModel


class TrainForm(forms.ModelForm):
    name = forms.CharField(
        label='Номер поезда',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Введите номер поезда'
        })
    )
    travel_time = forms.IntegerField(
        label='Время в пути',
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Время в пути'
        })
    )
    departure_city = forms.ModelChoiceField(
        label='Город отправления',
        queryset=CityModel.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    arrival_city = forms.ModelChoiceField(
        label='Город прибытия',
        queryset=CityModel.objects.all(),
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )

    class Meta:
        model = TrainModel
        fields = '__all__'
