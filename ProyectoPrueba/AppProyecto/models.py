from calendar import different_locale
from distutils.command.upload import upload
from http.client import PRECONDITION_FAILED
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH

from django.db import models

# Create your models here.
opcionesSexo = [
    [0,"Seleccione"],
    [1,"Hombre"],
    [2,"Mujer"],
    [3,"No especificado"]
]

class Usuario(models.Model):
    nombreusuario       = models.CharField(max_length=100)
    nombrereal          = models.CharField(max_length=10)
    RUT                 = models.CharField(primary_key=True,max_length=13)
    correo              = models.CharField(max_length=50)
    contrasena          = models.CharField(max_length=30)
    nacimiento          = models.DateField()
    genero              = models.IntegerField(choices=opcionesSexo)
    telefono            = models.CharField(max_length=100)
    Direccion           = models.TextField(max_length=100)
    comuna              = models.IntegerField()        
    
    def __str__(self):
        formato = "Username: {0} Nombre: ({1}) RUT: {2}"
        return formato.format(self.nombreusuario,self.nombrereal,self.RUT)
  

opcionescategoria = [
    [0,"Seleccione"],
    [1,"Macetas"],
    [2,"Plantas"],
    [3,"Herramientas"],
    [4,"Tierras"]
]

class Producto(models.Model):                                           #clase del Producto
    id_producto         = models.AutoField(primary_key=True)    #pk
    nombre_producto     = models.CharField(max_length=100)
    precio              = models.IntegerField()
    desc                = models.TextField(max_length=1000)
    stock               = models.IntegerField()
    categoria           = models.IntegerField(choices=opcionescategoria)                             #FK de la clase categoria
    FotoProducto        = models.ImageField(upload_to="productos", null=True)

    def __str__(self):
        return self.nombre_producto

class Detalle(models.Model):                                            #clase del Detalle
    id_detalle          = models.AutoField(primary_key=True)    #pk
    id_producto         = models.ForeignKey(Producto, null=True, blank=True, on_delete = models.CASCADE)#FK de la clase producto
    preciodetalle       = models.IntegerField()
    fechadetalle        = models.DateField()
    cantidad            = models.IntegerField()

    def __str__(self):
        formato = "detalle No: {} producto No{} cantidad:{}"
        return formato(self.id_detalle)

class boleta(models.Model):
    nombreBoleta        = models.TextField(max_length=12)