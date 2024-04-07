"""
from django.contrib import admin

# Register your models here.
"""

from django.contrib import admin
from .models import Vehiculo

class AdminVehiculo(admin.ModelAdmin):
    list_display = ['nombre', 'marca', 'modelo', 'anio', 'precio', 'image']  # Asegúrate de incluir 'image' aquí

admin.site.register(Vehiculo, AdminVehiculo)