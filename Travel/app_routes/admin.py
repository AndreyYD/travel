from django.contrib import admin
from .models import RouteModel

class RouteAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'departure_city', 'arrival_city', 'travel_time']

admin.site.register(RouteModel, RouteAdmin)
