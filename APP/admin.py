from django.contrib import admin
from .models import Contacto, Marca, Producto

# Register your models here.

admin.site.register(Marca)
admin.site.register(Producto)
admin.site.register(Contacto)