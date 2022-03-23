from django.contrib import admin
from .models import TrainModel

class TrainAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'departure_city', 'arrival_city', 'travel_time']

admin.site.register(TrainModel, TrainAdmin)
