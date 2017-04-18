from django.db import models
from django.contrib.auth.models import User
from accounts.models import Profile
from taggit.managers import TaggableManager
from django.db.models import Q
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
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
    slug = models.SlugField(max_length=200)

    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type

    def get_absolute_url(self):
        return reverse('product:detalle',args=[self.id,self.slug])

    def __str__(self):
        return self.titulo_anuncio

class Imagen_Anuncio(models.Model):
    Anuncio = models.ForeignKey(
        Anuncio,
        on_delete=models.CASCADE
    )
    imagen_anuncio = models.FileField(
        upload_to="productos/%Y/%m/%d"
    )


class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent=None)
        return qs

    def filter_by_instance(self,anuncio):
        content_type=   ContentType.objects.get_for_model(anuncio.__class__)
        obj_id =  anuncio.id
        qs = super(CommentManager, self).filter(content_type=content_type, object_id= obj_id).filter(parent=None)
        return qs


class Comment(models.Model):
    autor = models.ForeignKey(User, related_name="comentarios")
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    parent = models.ForeignKey("self", blank=True, null=True)
    fecha_comentario = models.DateTimeField(auto_now=True)
    cuerpo = models.TextField()
    objects = CommentManager()

    class meta:
        orden = ['-fecha_comentario']

    #def __str__(self):
    #    return '{} comento en {}'.format(self.autor,self.producto)

    def children(self):
        return Comment.objects.filter(parent=self)

    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True
