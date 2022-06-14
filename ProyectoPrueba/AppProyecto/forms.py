from pyexpat import model
from django import forms
from .models import Producto, Usuario

class ProductoForm(forms.ModelForm):

    FotoProducto = forms.FileField(widget=forms.FileInput(attrs={"class":"form-control"}))

    class Meta:
        model = Producto
        fields = '__all__'

class UsuarioForm(forms.ModelForm):
    nombreusuario =forms.CharField(widget = forms.TextInput(attrs= {"placeholder":"Ej: el_queso_bakan"}),required=True)
    nombrereal = forms.CharField(widget=forms.TextInput(attrs={"pattern":"[a-zA-Z ]*","placeholder":"Ej: Juan Pérez"}))
    RUT = forms.CharField(widget=forms.TextInput( attrs= {"oninput":"checkRut(this)","maxlength":"10","placeholder":"Ej: 12345678-5"}), required=True )
    correo = forms.CharField(widget=forms.EmailInput(attrs= {"placeholder":"Ingrese su Correo por favor"}), required=True)
    nacimiento = forms.DateField(widget=forms.DateInput(attrs= {"type":"date", }))
    contrasena = forms.CharField(widget=forms.PasswordInput(attrs= {"maxlength":"20","placeholder":"La contraseña debe tener por lo menos 8 Caracteres, procure no usar espacios"})) 
    telefono = forms.CharField(widget=forms.TextInput(attrs={"pattern":"[0-9]+", "maxlength":"10", "placeholder":"Ingrese su Telefono por favor"}))
    Direccion = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Ingrese su Direccion por favor"}))
    
    
    class Meta:
        model = Usuario
        fields= '__all__'
