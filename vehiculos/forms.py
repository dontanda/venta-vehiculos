from django import forms
from .models import Vehiculo # Vehicle

class VehiculoForm(forms.ModelForm):
    class Meta:
        model = Vehiculo  # Vehicle
        fields = ['nombre', 'marca', 'modelo', 'anio', 'precio', 'imagen'] # ['name', 'brand', 'model', 'year', 'price', 'image']