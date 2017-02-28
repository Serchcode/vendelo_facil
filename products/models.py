from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from taggit.managers import TaggableManager
from django.db.models import Q
# Create your models here.

class Categoria_Anuncio(models.Model):
    nombre_categoria = models.CharField(max_length=30)
    descripcion_categoria = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.nombre_categoria

class SubCategoria_Anuncio(models.Model):
    nombre_subcategoria = models.CharField(max_length=30)
    categoria = models.ForeignKey(Categoria_Anuncio, on_delete=models.CASCADE)
    descripcion_subcategoria = models.CharField(max_length=30)
    slug = models.SlugField()

    def __str__(self):
        return self.nombre_subcategoria

class Anuncio(models.Model):
    TIPO_MONEDA = (
        ('mxn','MXN'),
        ('usd','USD')
    )
    #tags = TaggableManager(blank = True , null=True)
    vendedor = models.ForeignKey(User, related_name="producto")
    titulo_anuncio = models.CharField(max_length=200)
    descripcion_anuncio = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Moneda = models.CharField(max_length=5, choices=TIPO_MONEDA)
    fecha_anuncio = models.DateField(auto_now=True)
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
    slug = models.SlugField(max_length=200)
    categoria = models.ForeignKey(
        Categoria_Anuncio,
        on_delete=models.CASCADE
    )
    subcategoria_relacion = models.ForeignKey(
        SubCategoria_Anuncio,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.titulo_anuncio

class Comment(models.Model):
    autor = models.ForeignKey(User, related_name="comentarios")
    producto = models.ForeignKey(Anuncio, related_name="producto")
    fecha_comentario = models.DateTimeField(auto_now=True)
    cuerpo = models.TextField()

    def __str__(self):
        return 'comento en {}.format(self.autor,self.producto)'
