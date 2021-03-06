from django import forms
from django.db.models import fields
from django.forms import widgets
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        #fields = ["nombre","correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__' #con esto llamamos a todos los campos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
    
        widgets ={
            "fecha_fabricacion": forms.SelectDateWidget()
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", "email", "password1", "password2" ]
    pass