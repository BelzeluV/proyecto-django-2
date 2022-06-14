from mailbox import NoSuchMailboxError
import random
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from . import models
from . import forms

# Create your views here.

def Inicio(request):
    productos = models.Producto.objects.all()
    return render(request,'Pagina/PaginaInicio.html',{'productos': productos})

def CrearCuenta(request):
    data = {"formulario" : forms.UsuarioForm}

    if request.method == 'POST':
        formulario = forms.UsuarioForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            data["formulario"] = formulario
    return render(request,"Pagina/PaginaRegistro.html",data)

def IniciarSesion(request):
    return render(request,"Pagina/PaginaInicioSesion.html")

def Busqueda(request,id):
    return render(request,'Pagina/Busqueda.html',)



def DetalleProd(request,id):
    Producto = get_object_or_404(models.Producto, id_producto = id)

    data = {"producto" : Producto}

    return render(request, 'Pagina/PaginaProducto.html', data)


def Vista(request):
    ListaDeProductos = models.Producto.objects.all() 
    page = request.GET.get('page',1)

    try:
        paginator = Paginator(ListaDeProductos, 5)
        ListaDeProductos = paginator.page(page)
    except:
        raise Http404

    data = {"entity": ListaDeProductos, 'paginator': paginator}

    return render(request, "CRUD/VISTA.html",data)

def Agregar(request):
    data = {"formulario" : forms.ProductoForm()}
    if request.method == 'POST':
        formulario = forms.ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="vista")
        else:
            data["formulario"] = formulario

    return render(request,"CRUD/AGREGAR.html", data)

def Modificar(request,id):

    producto = get_object_or_404(models.Producto, id_producto = id) 

    data = { "formulario" : forms.ProductoForm(instance = producto)}

    if request.method == 'POST':
        formulario = forms.ProductoForm(data = request.POST, instance=producto, files = request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect(to="vista")
        data["formulario"] = formulario

    return render(request,"CRUD/MODIFICAR.html",data)

def Eliminar(request,id):
    producto = get_object_or_404(models.Producto, id_producto = id) 
    producto.delete()
    return redirect(to="vista")