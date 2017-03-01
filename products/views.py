from django.views.generic import View
from .models import Anuncio, Comment, Categoria_Anuncio, SubCategoria_Anuncio
from .forms import AnuncioForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
import json


class ListViewAnuncio(View):
    def get(self, request, categoria=None):
        template_name = "products/list_products.html"
        anuncios = Anuncio.objects.all()
        tag = None
        if categoria:
            anuncios = Anuncio.objects.filter(categoria = categoria)
        context = {
            'anuncios':anuncios,
        }
        return render(request,template_name,context)

class AnuncioNuevo(View):
    """docstring for AnuncioNuevo Mostrar formulario para subir anuncio y guardar"""
    @method_decorator(login_required)
    def get(self, request):
        template_name = "products/formulario_anuncio.html"
        form = AnuncioForm()
        context ={
            'form':form,
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        template_name = "products/formulario_anuncio.html"
        form = AnuncioForm(data=request.POST, files=request.FILES)
        categoria=request.POST.get('Categoria_Anuncio')
        subcategoria=request.POST.get('subcategoria_relacion')
        print(categoria,':',subcategoria)
        print(form)
        if form.is_valid():
            print('hi')
            anuncio_nuevo = form.save(commit=False)
            anuncio_nuevo.slug = slugify(anuncio_nuevo.titulo_anuncio)
            anuncio_nuevo.vendedor = request.user
            anuncio_nuevo.Moneda = request.POST.get('Moneda')
            anuncio_nuevo.save()
            messages.success(request,'Anuncio Publicado')
            return redirect('product:lista')
        else:
            print("khe")
            messages.error(request,'No se guardo')
            context ={
                'form':form
            }
            return render(request, template_name, context)
