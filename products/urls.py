from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^lista/$', views.ListViewAnuncio.as_view(),name="lista"),
    url(r'^publicar', views.AnuncioNuevo.as_view(), name="nuevo")
]
