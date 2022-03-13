from django.urls import path
from .views import list_cities_view, CityDetailView

urlpatterns = [
    path('', list_cities_view, name='list_cities'),
    path('city/<int:pk>/', CityDetailView.as_view(), name='city'),
]
