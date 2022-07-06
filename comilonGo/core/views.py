from django.shortcuts import render
from .models import Producto, Categoria
from .forms import ProductoForm


def index(request):

    productos = Producto.objects.all()

    datos = {
        'productos' : productos
    }

    return render(request,'core/index.html',datos)

def menu(request):
    return render(request,'core/menu.html')

def producto(request):

    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    
    datos = {

        'categorias' : categorias,
        'productos' : productos
        
    }

    return render(request,'core/producto.html',datos)

def admin_productos(request):

    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    
    datos = {
        'categorias' : categorias,
        'productos' : productos
        
    }
    return render(request, 'core/admin_productos.html', datos)

def crear_producto(request):

    datos = {
        'form' : ProductoForm()
    }

    if request.method=='POST':
        
        formulario = ProductoForm(request.POST)
        codigoForm = formulario.data['codigo']

        try:
            codigoEncontrado = Producto.objects.get(codigo=codigoForm).codigo

        except Producto.DoesNotExist:
            codigoEncontrado = None

        if codigoEncontrado != None:

            datos['mensaje'] = "Ya existe el codigo"
            
        else:

            if formulario.is_valid:
 
                formulario.save()

                datos['mensaje'] = "Producto guardado correctamente"

    return render(request,'core/crear_producto.html', datos)