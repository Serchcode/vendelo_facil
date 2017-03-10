from django.conf.urls import url
from . import views
from .ajax import get_subcategoria_anuncio


urlpatterns = [
    url(r'^lista/$', views.ListViewAnuncio.as_view(),name="lista"),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)$', views.DetailView.as_view(), name="detalle"),
    url(r'^publicar/$', views.AnuncioNuevo.as_view(), name="publicar"),
    url(r'^ajax/get_subcategoria/$', get_subcategoria_anuncio, name="get_subcategoria"),
]
