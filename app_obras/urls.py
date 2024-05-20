from django.urls import path, include
from app_obras.views import *

urlpatterns = [
    path('', index,name='index'),
    path('nosotros.html', nosotros,name='nosotros'),
    path('galeria.html', galeria,name='galeria'),
    path('administracion.html', administracion,name='administracion'),
    path('crear.html', crear,name='crear'),
    path('mostrar.html', mostrar,name='mostrar'),
    path('eliminar/<obra_id>', eliminar, name="eliminar"),
    path('modificar/<obra_id>', modificar, name="modificar"),


    path('generarBoleta/', generarBoleta,name="generarBoleta"),
    path('agregar/<id>', agregar_producto, name="agregar"),
    path('eliminar/<id>', eliminar_producto, name="eliminar"),
    path('restar/<id>', restar_producto, name="restar"),
    path('limpiar/', limpiar_carrito, name="limpiar"),
    
]