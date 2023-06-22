from distutils.command.upload import upload
from django.db import models

# Create your models here.
class Categoria (models.Model):
    idCategoria = models.IntegerField (primary_key=True, verbose_name= 'Id de Categoria')
    nombreCategoria = models.CharField(max_length=50,verbose_name='Nombre de Categoria')

    def __str__(self):
        return self.nombreCategoria
    
class Obra (models.Model):
    idObra= models.CharField(max_length=6, primary_key=True, verbose_name='Id de Obra')
    autor= models.CharField(max_length=20,verbose_name='Autor')
    titulo= models.CharField(max_length=40, verbose_name='Titulo de obra')
    imagen= models.ImageField(upload_to='imagenes', null=True, blank=True,verbose_name='Imagen')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria")

    def __str__(self):
        return self.idObra




