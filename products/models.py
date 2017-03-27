from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from taggit.managers import TaggableManager
from django.db.models import Q
from django.core.urlresolvers import reverse
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
    vendedor = models.ForeignKey(User, related_name="productos")
    titulo_anuncio = models.CharField(max_length=200)
    descripcion_anuncio = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    Moneda = models.CharField(
        max_length=5,
        choices=TIPO_MONEDA,
    )
    categoria = models.ForeignKey(
        Categoria_Anuncio,
        on_delete=models.CASCADE,
    )
    subcategoria_relacion = models.ForeignKey(
        SubCategoria_Anuncio,
        on_delete=models.CASCADE,
    )
    fecha_anuncio = models.DateField(auto_now=True)
    imagen_principal = models.ImageField(upload_to="productos/%Y/%m/%d")
    imagen_secundaria = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_terciaria = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_uno = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_dos = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_tres = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_cuatro = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_cinco = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_seis = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_siete = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_ocho = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_nueve = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_diez = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_once = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    imagen_opcional_doce = models.ImageField(
        upload_to="productos/%Y/%m/%d",
        blank=True,
        null=True
    )
    slug = models.SlugField(max_length=200)

    def get_absolute_url(self):
        return reverse('product:detalle',args=[self.slug])

    def __str__(self):
        return self.titulo_anuncio


class Comment(models.Model):
    autor = models.ForeignKey(User, related_name="comentarios")
    producto = models.ForeignKey(Anuncio, related_name="procoment")
    fecha_comentario = models.DateTimeField(auto_now=True)
    cuerpo = models.TextField()

    def __str__(self):
        return 'comento en {}.format(self.autor,self.producto)'

class Answer(models.Model):
    replied = models.ForeignKey(User, related_name="respuesta")
    respuesta = models.ForeignKey(Comment, related_name="respuesta_comentario")
    fecha = models.DateTimeField(auto_now=True)
    pregunta = models.TextField()

    def __str__(self):
        return 'respuestua en {}.format(self.replied,self.respuesta)'