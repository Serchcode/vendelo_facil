from django.contrib import admin
from .models import Product, Comment
# Register your models here.
def make_published(modeladmin, request, queryset):
    queryset.update(categoria='productos')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['vendedor','nombre_producto','tags']
    ordering = ['nombre_producto']
    actions = [make_published]
admin.site.register(Product, ProductAdmin)
