from django import forms
from .models import Obra
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class RegistroUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = [ 'username', 'first_name', 'last_name', 'email', 'password1', 'password2']

class ObraForm(forms.ModelForm):
    class Meta:
        model = Obra 
        fields = ['idObra', 'autor', 'titulo', 'categoria', 'imagen']
        labels ={
            'idObra':'IdObra',
            'autor' : 'Autor',
            'titulo': 'Titulo',
            'categoria':'Categoria',
            'imagen':'Imagen'
        }
        widgets={

            'idObra':forms.TextInput(
                attrs={
                    'placeholder':'Ingrese el Id..',
                    'id': 'id',
                    'class': 'form-control',
                }
            ),
            'autor': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese autor..',
                    'id':'autor',
                    'class':'form-control',
                }
            ),
            'titulo': forms.TextInput(
                attrs={
                    'placeholder':'Ingrese titulo..',
                    'id':'titulo',
                    'class':'form-control',
                }
            ),
            'categoria': forms.Select(
                attrs={
                    'id':'categoria',
                    'class':'form-control',
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class':'form-control',
                    'id': 'imagen',
                }
            )
        }