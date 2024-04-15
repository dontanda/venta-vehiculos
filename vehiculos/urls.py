# urls.py de la aplicaci�n
from django.urls import path
from .views import vehicle_list, vehicle_detail, add_vehicle, edit_vehicle, delete_vehicle

urlpatterns = [
    path('', vehicle_list, name='vehicle_list'),  # Lista de veh�culos    
    path('<int:vehicle_id>/', vehicle_detail, name='vehicle_detail'),  # Detalle de veh�culo
    path('add/', add_vehicle, name='add_vehicle'),  # Agregar veh�culo
    path('edit/<int:vehicle_id>/', edit_vehicle, name='edit_vehicle'),  # Editar veh�culo
    path('delete/<int:vehicle_id>/', delete_vehicle, name='delete_vehicle'),  # Eliminar veh�culo
]