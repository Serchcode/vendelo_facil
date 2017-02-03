from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from taggit.managers import TaggableManager
# Create your models here.

class Product(models.Model):
    CATEGORIAS_PRODUCTO = (
        ('vehiculos','Veículos'),
        ('inmuebles','Inmuebles'),
        ('servicios','Servicios'),
        ('productos','Productos y otros'),
    )
    nombre_producto = models.CharField(max_length=30)
    tags = TaggableManager()
    vendedor = models.ForeignKey(User, related_name="producto")
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=2, decimal_places=2)
    fecha_producto = models.DateTimeField(auto_now=True)
    imagen_principal = models.ImageField(upload_to="productos")
    imagen_secundaria = models.ImageField(upload_to="productos")
    imagen_terciaria = models.ImageField(upload_to="productos")
    imagen_opcional_uno = models.ImageField(
        upload_to="productos",
        blank=True,
        null=True
    )
    imagen_opcional_dos = models.ImageField(
        upload_to="productos",
        blank=True,
        null=True
    )
    imagen_opcional_tres = models.ImageField(
        upload_to="productos",
        blank=True,
        null=True
    )
    categoria = models.CharField(
        max_length=20,
        choices=CATEGORIAS_PRODUCTO
    )
    slug = models.SlugField(max_length=200)

    def __str__(self):
        return self.nombre_producto


class Comment(models.Model):
    autor = models.ForeignKey(User, related_name="comentarios")
    producto = models.ForeignKey(Product, related_name="producto")
    fecha_comentario = models.DateTimeField(auto_now=True)
    cuerpo = models.TextField()

    def __str__(self):
        return 'comento en {}.format(self.autor,self.producto)'
