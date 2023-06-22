from django.urls import path, include
from .views import index, nosotros,galeria,administracion,crear,mostrar, eliminar, modificar

urlpatterns = [
    path('', index,name='index'),
    path('nosotros.html', nosotros,name='nosotros'),
    path('galeria.html', galeria,name='galeria'),
    path('administracion.html', administracion,name='administracion'),
    path('crear.html', crear,name='crear'),
    path('mostrar.html', mostrar,name='mostrar'),
    path('eliminar/<obra_id>', eliminar, name="eliminar"),
    path('modificar/<obra_id>', modificar, name="modificar"),
    
]