from django.db import models

# Create your models here.

class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True,verbose_name='Id de categoria')
    nombreCategoria = models.CharField(max_length=50, verbose_name='Nombre de la Categoria')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    codigo = models.CharField(max_length=6,primary_key=True,verbose_name='Codigo')
    descripcion = models.CharField(max_length=20,verbose_name='Descripcion')
    precio = models.CharField(max_length=12, null=False,blank=False, verbose_name='Precio')
    imagen = models.CharField(max_length=250,null=True,blank=False, verbose_name='Imagen')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.codigo