from django.contrib.auth.decorators import login_required,permission_required
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate,login
from django.core.paginator import Paginator
from django.contrib import messages
from rest_framework import viewsets
from django.http import Http404
from . import serializers
from . import Carrito
from . import models
from . import forms

class ProductoViewset(viewsets.ModelViewSet):
    queryset = models.Producto.objects.all()
    serializer_class = serializers.ProductoSerializer

class MarcaViewset(viewsets.ModelViewSet):
    queryset = models.Marca.objects.all()
    serializer_class = serializers.MarcaSerializer

class CategoriaViewset(viewsets.ModelViewSet):
    queryset = models.Categoria.objects.all()
    serializer_class = serializers.CategoriaSerializer

class PedidoViewset(viewsets.ModelViewSet):
    queryset = models.Pedido.objects.all()
    serializer_class = serializers.PedidoSerializer

class LineaPedidoViewset(viewsets.ModelViewSet):
    queryset = models.LineaPedido.objects.all()
    serializer_class = serializers.LineaPedidoSerializer

class UsuarioViewset(viewsets.ModelViewSet):
    queryset = models.Usuario.objects.all()
    serializer_class = serializers.UsuarioSerializer

class ContactoViewset(viewsets.ModelViewSet):
    queryset = models.Contacto.objects.all()
    serializer_class = serializers.UsuarioSerializer


#Vista de Usuario Normal



def Inicio(request):
    listadoCategorias = models.Categoria.objects.all
    productos = models.Producto.objects.all()
    return render(request,'Pagina/PaginaInicio.html',{'productos': productos, "lista":listadoCategorias})

def Busqueda(request,nombre):
    listadoCategorias = models.Categoria.objects.all
    productos = models.Producto.objects.all()
    data = {"listaP" : productos, "lista":listadoCategorias}
    return render(request,'Pagina/Busqueda.html',data)

def DetalleProd(request,id):
    listadoCategorias = models.Categoria.objects.all
    Producto = get_object_or_404(models.Producto, id_producto = id)
    data = {"producto" : Producto,"lista":listadoCategorias}
    return render(request, 'Pagina/PaginaProducto.html', data)

def Contacto(request):
    data = {"formulario" : forms.ContactoForm()}
    if request.method == 'POST':
        formulario = forms.ContactoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Su Mensaje Fue enviado con exito")
            return redirect(to="home")
        else:
            data["formulario"] = formulario
    return render(request,"Pagina/PaginaContacto.html", data)

def registro(request):
    data = {"form" : forms.CustomUsercreationForm()}

    if request.method == 'POST':
        formulario = forms.CustomUsercreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login(request,user)
            messages.success(request,"Logueado correctamente")
            return redirect(to="home")
        else:
            data["form"] = formulario
    return render(request, 'registration/registro.html',data)


#vista carrito(no requiere permisos)

def Carro(request):
    return render(request,"Pagina/carro/Carro.html")

def agregar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = models.Producto.objects.get(id_producto = id)
    carro.agregar(Producto = producto)
    return redirect(to="carro")

def eliminar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = models.Producto.objects.get(id_producto = id)
    carro.eliminar(Producto = producto)
    return redirect(to="carro")

def restar_producto(request,id):
    carro = Carrito.Carro(request)
    producto = models.Producto.objects.get(id_producto = id)
    carro.restar_producto(Producto = producto)
    return redirect(to="carro")

def vaciar_carro(request):
    carro = Carrito.Carro(request)
    carro.limpiar_carro()
    return redirect("")

#pagar carrito (requiere login)
@login_required
def procesar_pedido(request):

    data = {"formulario" : forms.UsuarioForm}

    if request.method == 'POST':
        formulario = forms.UsuarioForm(data=request.POST, files = request.FILES)
        if formulario.is_valid():
            obj = formulario.save(commit = False) 
            obj.user = request.user; 
            obj.save()


            Pedido = models.Pedido.objects.create(user = request.user)
            carrito = Carrito.Carro(request)
            lineas_pedido = list()


            for key,value in carrito.carro.items():
                lineas_pedido.append(models.LineaPedido.objects.create(
                    user = request.user,
                    id_producto = models.Producto.objects.get(id_producto = key),
                    cantidad = value["cantidad"],
                    pedido_id = models.Pedido.objects.get(id= Pedido.id)))            
            carrito.limpiar_carro()
            messages.success(request,"Su Pedido Fue Realizado con exito, Pronto te contactaremos cuando se compruebe el pago")
            return redirect(to = "home")


        else:
            data["formulario"] = formulario

    return render(request, "Pagina/carro/Direccionpedido.html",data)

#leer contacto de usuarios

def Contactovista(request):
    listacontactos = models.Contacto.objects.all()
    page = request.GET.get('page',1)
    data = { "entity" : listacontactos}

    return render(request,"Mensajes/mensajesrec.html",data)





#Productos CRUD
@permission_required('AppProyecto.view_Producto')
def Vista(request):
    ListaDeProductos = models.Producto.objects.all() 
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(ListaDeProductos, 5)
        ListaDeProductos = paginator.page(page)
    except:
        raise Http404
    data = {"entity": ListaDeProductos, 'paginator': paginator}
    return render(request, "CRUD/Productos/VISTA.html",data)

@permission_required('AppProyecto.add_Producto')
def Agregar(request):
    data = {"formulario" : forms.ProductoForm()}
    if request.method == 'POST':
        formulario = forms.ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Producto agregado con exito")
            return redirect(to="vista")
        else:
            data["formulario"] = formulario
    return render(request,"CRUD/Productos/AGREGAR.html", data)

@permission_required('AppProyecto.change_Producto')
def Modificar(request,id):
    producto = get_object_or_404(models.Producto, id_producto = id) 
    data = { "formulario" : forms.ProductoForm(instance = producto)}
    if request.method == 'POST':
        formulario = forms.ProductoForm(data = request.POST, instance=producto, files = request.FILES)
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Producto modificado con exito")
            return redirect(to="vista")
        data["formulario"] = formulario
    return render(request,"CRUD/Productos/MODIFICAR.html",data)

@permission_required('AppProyecto.delete_Producto')
def Eliminar(request,id):
    producto = get_object_or_404(models.Producto, id_producto = id) 
    producto.delete()
    messages.success(request,"Producto Eliminado Con Exito")
    return redirect(to = "vista")


#Marcas CRUD
@permission_required('AppProyecto.view_Marca','AppProyecto.add_Marca')
def CRUD_Marcas(request):
    listaMarcas = models.Marca.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(listaMarcas, 3)
        listaMarcas = paginator.page(page)
    except:
        raise Http404
    data = {"formulario" : forms.MarcaForm(), "entity" : listaMarcas, 'paginator': paginator}
    if request.method == 'POST':
        formulario = forms.MarcaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()  
            messages.success(request,"Marca Agregada Con Exito")  
            return redirect(to = "crud-marcas") 
        else:
            data["formulario"] = formulario
    return render(request,"CRUD/Marcas/crudMARCAS.html",data)

@permission_required('AppProyecto.delete_Marca')
def EliminarMarca(request,id):
    marca = get_object_or_404(models.Marca,id_marca = id)
    marca.delete()
    messages.success(request,"Marca Eliminada con exito")
    return redirect(to = "crud-marcas")

@permission_required('AppProyecto.change_Marca')
def ModificarMarca(request,id):
    marca = get_object_or_404(models.Marca, id_marca = id)
     
    data = { "formulario" : forms.MarcaForm(instance = marca)}

    if request.method == 'POST':
        formulario = forms.MarcaForm(data = request.POST, instance=marca)
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Marca Modificada Con Exito")
            return redirect(to="crud-marcas")
        data["formulario"] = formulario
    return render(request, "CRUD/Marcas/editarMARCAS.html",data)


#categorias CRUD
@permission_required('AppProyecto.view_Categoria','AppProyecto.add_Categoria')
def CRUD_Categorias(request):
    lista = models.Categoria.objects.all()
    page = request.GET.get('page',1)
    try:
        paginator = Paginator(lista, 5)
        lista = paginator.page(page)
    except:
        raise Http404
    data = {"formulario" : forms.CategoriaForm(), "entity" : lista, 'paginator': paginator}
    if request.method == 'POST':
        formulario = forms.CategoriaForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Categoria Agregada con exito")
            return redirect(to = "crud-categorias") 
        else:
            data["formulario"] = formulario
    return render(request,"CRUD/Categorias/crudCATEGORIAS.html",data)

@permission_required('AppProyecto.delete_Categoria')
def EliminarCategoria(request,id):
    categoria = get_object_or_404(models.Categoria,id_categoria = id)
    categoria.delete()
    messages.success(request,"Categoria Eliminada con Exito")
    return redirect(to = "crud-categorias")

@permission_required('AppProyecto.change_Categoria')
def ModificarCategoria(request,id):
    categoria = get_object_or_404(models.Categoria, id_categoria = id) 
    data = { "formulario" : forms.CategoriaForm(instance = categoria)}

    if request.method == 'POST':
        formulario = forms.CategoriaForm(data = request.POST, instance = categoria)
        if formulario.is_valid:
            formulario.save()
            messages.success(request,"Categoria Modificada con exito")
            return redirect(to = "crud-categorias")
        data["formulario"] = formulario
    return render(request, "CRUD/Categorias/editarCATEGORIAS.html",data)