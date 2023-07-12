from django.shortcuts import render, redirect
from .models import Obra, Boleta, detalle_boleta
from .forms import ObraForm, RegistroUserForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from app_obras.compra import Carrito
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



def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    obra = Obra.objects.get(idObra=id)
    carrito_compra.agregar(obra=obra)
    return redirect('mostrar')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    obra = Obra.objects.get(idObra=id)
    carrito_compra.eliminar(obra=obra)
    return redirect('mostrar')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    obra = Obra.objects.get(idObra=id)
    carrito_compra.restar(obra=obra)
    return redirect('mostrar')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('mostrar')    


def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Obra.objects.get(idObra = value['obra_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)