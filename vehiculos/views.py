"""
from django.shortcuts import render

# Create your views here.
"""

from django.shortcuts import render, redirect
from .models import Vehiculo # Vehicle
from .forms import VehiculoForm # VehicleForm

def vehicle_list(request):
#    vehicles = Vehicle.objects.all()
#    return render(request, 'vehicle_list.html', {'vehicle_list': vehicles})
    vehiculos = Vehiculo.objects.all()
    return render(request, 'list_vehiculo.html', {'list_vehiculo': vehiculos})

def vehicle_detail(request, vehicle_id):
#    vehicle = Vehicle.objects.get(id=vehicle_id)
#    return render(request, 'vehicle_detail.html', {'vehicle': vehicle})
    vehiculo = Vehiculo.objects.get(id=vehicle_id)
    return render(request, 'det_vehiculo.html', {'vehiculo': vehiculo})
    
def add_vehicle(request):
    if request.method == 'POST':
        form = VehiculoForm(request.POST, request.FILES)   #        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehiculoForm() # form = VehicleForm()
    return render(request, 'agg_vehiculo.html', {'form': form})  # render(request, 'add_vehicle.html', {'form': form})

def edit_vehicle(request, vehicle_id):
    vehiculo = Vehiculo.objects.get(id=vehicle_id)   # vehicle = Vehicle.objects.get(id=vehicle_id)
    if request.method == 'POST':
        form = VehiculoForm(request.POST, instance=vehiculo)    # form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')
    else:
        form = VehiculoForm(instance=vehiculo)  # form = VehicleForm(instance=vehicle)
    return render(request, 'edit_vehiculo.html', {'form':form}) # render(request, 'edit_vehicle.html', {'form': form})

def delete_vehicle(request, vehicle_id):
    vehiculo = Vehiculo.objects.get(id=vehicle_id)
    vehiculo.delete()
    return redirect('vehicle_list')