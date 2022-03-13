from django.contrib import admin
from .models import CityModel

class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']

admin.site.register(CityModel, CityAdmin)
