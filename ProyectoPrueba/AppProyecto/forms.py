from django import forms
from .models import Categoria, Contacto, Marca, Producto, Usuario
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductoForm(forms.ModelForm):

    FotoProducto    = forms.FileField(widget = forms.FileInput(attrs={"class":"form-control"}))

    class Meta:
        model       = Producto
        fields      = '__all__'

class UsuarioForm(forms.ModelForm):
    nombrereal      = forms.CharField(widget = forms.TextInput(attrs = {"pattern":"[a-zA-Z ]*","placeholder":"Ej: Juan Pérez"}))
    RUT             = forms.CharField(widget = forms.TextInput( attrs = {"oninput":"checkRut(this)","maxlength":"10","placeholder":"Ej: 12345678-5"}), required=True)
    telefono        = forms.CharField(widget = forms.TextInput(attrs = {"pattern":"[0-9]+", "maxlength":"10", "placeholder":"Ingrese su Telefono por favor"}))
    Direccion       = forms.CharField(widget = forms.TextInput(attrs = {"placeholder":"Ingrese su Direccion por favor"}))
    
    
    class Meta:
        model       = Usuario
        fields      = ['nombrereal','RUT', 'telefono', 'Direccion', 'comuna' ,'mediopago']

class MarcaForm(forms.ModelForm):
    class Meta:
        model       = Marca
        fields      = '__all__'

class CategoriaForm(forms.ModelForm):
    class Meta:
        model       = Categoria
        fields      = '__all__'

class ContactoForm(forms.ModelForm):
    class Meta:
        model       = Contacto
        fields      = '__all__'

class CustomUsercreationForm(UserCreationForm):
    class Meta:
        model       = User
        fields      = ['username',"first_name", "last_name", "email", "password1", "password2"]