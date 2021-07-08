from django.core import paginator
from django.http.response import Http404
from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Marca
from .forms import ContactoForm, ProductoForm, CustomUserCreationForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.http import Http404
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def home (request):
    productos = Producto.objects.order_by('-id')[0:3]
    secundarios = Producto.objects.order_by('-id')[3:10]
   
   
    data = {
        'productos': productos,
        'secundarios': secundarios,
        
    }
    return render(request, 'app/home.html', data)

def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Contacto enviado"
        else:
            data ["form"] = formulario
            
    return render(request, 'app/contacto.html', data)

def galeria(request):
    todos = Producto.objects.all()
    data ={
         'todos': todos
     }
    return render(request, 'app/galeria.html', data)
@permission_required('APP.add_producto')
def agregar_producto(request):
    data ={
        'form': ProductoForm()
    }
    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Producto agregado correctamente")           
        else:
            data["form"] = formulario

    return render(request, 'producto/agregar.html', data)
@permission_required('APP.view_producto')
def listar_productos(request):
    productos = Producto.objects.all()
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(productos, 5)
        productos = paginator.page(page)
    except:
        raise Http404    
    data = {
        'entity': productos,
        'paginator': paginator
    }

    return render (request, 'producto/listar.html', data)
@permission_required('APP.change_producto')
def modificar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    data= {
        'form': ProductoForm(instance= producto)
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST,instance=producto, files=request.FILES)
        if formulario.is_valid:
            formulario.save()
            messages.success(request, "Producto modificado correctamente")
            return redirect(to="listar_productos")
        data['form'] = formulario

    return render(request, 'producto/modificar.html', data)
@permission_required('APP.delete_producto')
def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    messages.success(request, "Producto eliminado correctamente")
    return redirect(to="listar_productos")

def registro(request):

    data= {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data= request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username= formulario.cleaned_data["username"], password = formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect (to="home")
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)

def buscar(request):
    if request.method == "POST":
        buscador = request.POST['buscador']
        productos = Producto.objects.filter(nombre__contains = buscador)
        return render (request, 'app/busqueda.html',{ 'buscador': buscador, 'productos': productos })
    else:
        return render (request, 'app/busqueda.html',{})

def detalle(request, id):
    prod = Producto.objects.all().get(pk=id)
    return render(request, 'app/detalle.html', {'prod':prod})


