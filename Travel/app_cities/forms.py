from django import forms
from .models import CityModel


class CityForm(forms.Form):
    name = forms.CharField(label='Город')

class CityModelForm(forms.ModelForm):
    name = forms.CharField(label='Город', widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Введите название города',
    }))

    class Meta:
        model = CityModel
        fields = ('name', )
