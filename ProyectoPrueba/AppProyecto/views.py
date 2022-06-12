from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import Context
from django.template import loader
from . import models
from . import forms
# Create your views here.

def Inicio(request):
    productos = models.Producto.objects.all()
    return render(request,'Pagina/PaginaInicio.html',{'productos': productos})

def CrearCuenta(request):
    return render(request,"Pagina/PaginaRegistro.html")

def IniciarSesion(request):
    return render(request,"Pagina/PaginaInicio.html")

def Busqueda(request):
    return render(request,'Pagina/Busqueda.html')

def Vista(request):
    ListaDeProductos = models.Producto.objects.all() 
    return render(request, "CRUD/VISTA.html",{"productos":ListaDeProductos})

def Agregar(request):
    data = {"formulario" : forms.ProductoForm()}
    if request.method == 'POST':
        formulario = forms.ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Producto Guardado"
        else:
            data["formulario"] = formulario

    return render(request,"CRUD/AGREGAR.html", data)

def Modificar(request,id):

    producto = get_object_or_404(Producto, id = id) 

    data = { "formulario" : ProductoForm(instance = producto)}

    if request.method == 'POST':
        formulario = ProductoForm(data = request.POST, instance=producto, files = request.FILES)
        if formulario.is_valid:
            formulario.save()
            return redirect(to="vista")
        data["formulario"] = formulario

    return render(request,"CRUD/MODIFICAR.html",data)

def Eliminar(request,id):
    return rendeer(request,"CRUD/ELIMINAR.html")