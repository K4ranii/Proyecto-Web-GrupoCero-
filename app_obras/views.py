from django.shortcuts import render, redirect
from .models import Obra
from .forms import ObraForm, RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
def index(request):
	obras= Obra.objects.all()
	
	return render(request, 'index.html',context={'datos':obras})


def nosotros(request):
	obras= Obra.objects.all()
	
	return render(request, 'nosotros.html',context={'datos':obras})

def galeria(request):
	obras= Obra.objects.all()
	
	return render(request, 'galeria.html',context={'datos':obras})

def administracion(request):
	obras= Obra.objects.all()
	
	return render(request, 'administracion.html',context={'datos':obras})

@login_required
def crear(request):
    if request.method=="POST":
        obraform=ObraForm(request.POST,request.FILES)
        if obraform.is_valid():
            obraform.save()     #similar al insert en función
            return redirect ('administracion')
    else:
        obraform=ObraForm()
    return render (request, 'crear.html', {'obraform': obraform})

def mostrar(request):
	obras= Obra.objects.all()
	
	return render(request, 'mostrar.html',context={'datos':obras})

@login_required
def eliminar(request, obra_id): 
    obraEliminada = Obra.objects.get(idObra=obra_id) #similar a select * from... where...
    obraEliminada.delete()
    return redirect ('administracion')

@login_required
def modificar(request, obra_id): 
    obraModificada = Obra.objects.get(idObra=obra_id) # Buscamos el objeto
    
    if request.method == "POST":
        formulario = ObraForm(data=request.POST, instance=obraModificada)
        if formulario.is_valid():
            formulario.save()
            return redirect('administracion')
    else:
        # Crear el formulario con el atributo readonly
        form = ObraForm(instance=obraModificada)
        form.fields['idObra'].widget.attrs['readonly'] = 'readonly'

    datos = {
        'form': form
    }
    
    return render(request, 'modificar.html', datos)


def mostrar(request):
    obras = Obra.objects.all()
    datos={
        'obras':obras
    }
    return render(request, 'mostrar.html', datos)

# Create your views here.
