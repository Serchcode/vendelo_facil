from django.contrib import admin
from .models import Anuncio, Comment, Categoria_Anuncio, SubCategoria_Anuncio
# Register your models here.
def make_published(modeladmin, request, queryset):
    queryset.update(categoria='productos')

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['vendedor','titulo_anuncio']
    ordering = ['fecha_anuncio']
    actions = [make_published]

admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Categoria_Anuncio)
admin.site.register(SubCategoria_Anuncio)
