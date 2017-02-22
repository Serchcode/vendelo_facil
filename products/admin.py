from django.contrib import admin
from .models import Anuncio, Comment, Categoria_Anuncio, SubCategoria_Anuncio
# Register your models here.
def make_published(modeladmin, request, queryset):
    queryset.update(categoria='productos')

class AnuncioAdmin(admin.ModelAdmin):
    list_display = ['vendedor','titulo_anuncio']
    ordering = ['fecha_anuncio']
    actions = [make_published]
    prepopulated_fields = {"slug": ("titulo_anuncio",)}

class CategoriaAnuncioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre_categoria",)}

class SubcategoriaAnuncioAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("nombre_subcategoria",)}

admin.site.register(Anuncio, AnuncioAdmin)
admin.site.register(Categoria_Anuncio, CategoriaAnuncioAdmin)
admin.site.register(SubCategoria_Anuncio, SubcategoriaAnuncioAdmin)
