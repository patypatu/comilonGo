from django.urls import path
from .views import index,menu,producto,admin_productos,crear_producto,mod_producto,del_producto

urlpatterns = [
    path('',index,name="index"),
    path('index.html',index,name="index"),
    path('menu.html',menu,name="menu"),
    path('producto.html',producto,name="producto"),
    path('admin_productos.html',admin_productos,name="admin_productos"),
    path('crear_producto.html',crear_producto,name="crear_producto"),
    path('mod_producto.html/<id>',mod_producto,name="mod_producto"),
    path('del_producto.html/<id>',del_producto,name="del_producto"),
]