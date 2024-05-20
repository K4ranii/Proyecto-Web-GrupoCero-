from rest_framework import serializers
from .models import Categoria, Obra, Boleta, detalle_boleta

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categoria
        fields = '__all__'

class ObraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Obra
        fields = '__all__'

class BoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boleta
        fields = '__all__'

class DetalleBoletaSerializer(serializers.ModelSerializer):
    class Meta:
        model = detalle_boleta
        fields = '__all__'