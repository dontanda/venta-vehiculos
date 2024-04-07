# from django.db import models
# 
# # Create your models here.
# 

from django.db import models

class Vehiculo(models.Model):
    nombre = models.CharField(max_length=100)
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='imagenes/')
    
    def __str__(self):
        return self.nombre + ' ' + self.modelo