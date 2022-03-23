from django.urls import path
from .views import list_cities_view, CityDetailView, CityCreateView, CityUpdateView, CityDeleteView, CityListView

app_name = 'app_cities'

urlpatterns = [
    path('', CityListView.as_view(), name='list_cities'),
    path('city/<int:pk>/', CityDetailView.as_view(), name='city'),
    path('add/', CityCreateView.as_view(), name='create'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
]
