from .models import Producto, Marca

def menu_categoria(request):
    categorias = Marca.objects.all()
    return ({"categorias": categorias})