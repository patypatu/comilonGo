from django.shortcuts import render, redirect
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

def mod_producto(request,id):

    datos = {
        
    }
    
    datos['mensaje'] = ""
    producto = Producto.objects.get(codigo=id)

    if request.method=='POST':

        formulario = ProductoForm(data=request.POST,instance=producto)

        if formulario.is_valid:
            if Producto.objects.get(codigo=id) != formulario.data['codigo']:

                formulario.save()

                datos['mensaje'] = "Producto Modificado Correctamente"

    

    datos['form'] = ProductoForm(instance=producto)

    return render(request, 'core/mod_producto.html',datos)

def del_producto(request,id):

    producto = Producto.objects.get(codigo=id)

    producto.delete()

    return redirect(to="../admin_productos.html")