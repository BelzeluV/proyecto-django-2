from calendar import different_locale
from distutils.command.upload import upload
from http.client import PRECONDITION_FAILED
from tkinter import CASCADE
from unittest.util import _MAX_LENGTH

from django.db import models

# Create your models here.
opcionesSexo = [
    [0,"Hombre"],
    [1,"Mujer"],
    [2,"No especificado"]
]

opcionesmetodopago= [
    [0, "efectivo"],
    [1, "tarjeta de Credito"],
    [2, "tarjeta de Debito"],
    [3, "transferencia"],
    [4, "prepago"],
    [5, ""],
    
]

opcionescomuna =[
    [0,"Peñaflor"],
    [1,"Cerrillos"],
    [2,"Cerro Navia"],
    [3,"Conchalí"],
    [4,"El Bosque"],
    [5,"Estación Central"],
    [6,"Huechuraba"],
    [7,"Independencia"],
    [8,"La Cisterna"],
    [9,"La Florida"],
    [10,"La Granja"],
    [11,"La Pintana"],
    [12,"La Reina"],
    [13,"Las Condes"],
    [14,"Lo Barnechea"],
    [15,"Lo Espejo"],
    [16,"Lo Prado"],
    [17,"Macul"],
    [18,"Maipú"],
    [19,"Ñuñoa"],
    [20,"Pedro Aguirre Cerda"],
    [21,"Peñalolén"],
    [22,"Providencia"],
    [23,"Pudahuel"],
    [24,"Quilicura"],
    [25,"Quinta Normal"],
    [26,"Recoleta"],
    [27,"Renca"],
    [28,"San Joaquín"],
    [29,"San Miguel"],
    [30,"San Ramón"],
    [31,"Vitacura"],
    [32,"Puente Alto"],
    [33,"Pirque"],
    [34,"San José de Maipo"],
    [35,"Colina"],
    [36,"Lampa"],
    [37,"Tiltil"],
    [38,"San Bernardo"],
    [39,"Buin"],
    [40,"Calera de Tango"],
    [41,"Paine"],
    [42,"Melipilla"],
    [43,"Alhué"],
    [44,"Curacaví"],
    [45,"María Pinto"],
    [46,"San Pedro"],
    [47,"Talagante"],
    [48,"El Monte"],
    [49,"Isla de Maipo"],
    [50,"Padre Hurtado"],
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
    Direccion           = models.CharField(max_length=100)
    comuna              = models.IntegerField(choices=opcionescomuna)        
    
    def __str__(self):
        formato = "Username: {0} Nombre: ({1}) RUT: {2}"
        return formato.format(self.nombreusuario,self.nombrereal,self.RUT)
 

opcionescategoria = [
    
    [0,"Macetas"],
    [1,"Plantas"],
    [2,"Herramientas"],
    [3,"Tierras"]
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
    id_boleta           = models.AutoField(primary_key=True)
    id_producto         = models.ForeignKey(Producto, null=True, blank=True, on_delete = models.CASCADE)
    rut                 = models.ForeignKey(Usuario, null=True, blank=True, on_delete = models.CASCADE)
    id_detalle          = models.ForeignKey(Detalle, null=True, blank=True, on_delete = models.CASCADE)
