from django.views.generic import View
from .models import Anuncio, Comment, Categoria_Anuncio, SubCategoria_Anuncio
from .forms import AnuncioForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
import json
from django.http import HttpResponseRedirect


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
        if request.method == 'POST':
            data = request.POST
            files = request.FILES
            print(files)
            print(data)
            form = AnuncioForm(data, files)
            print(form)
            if form.is_valid():
                anuncio_nuevo = form.save(commit=False)
                print('hola')
                anuncio_nuevo.slug = slugify(anuncio_nuevo.titulo_anuncio)
                anuncio_nuevo.Moneda = request.POST.get('Moneda')
                anuncio_nuevo.vendedor = request.user
                anuncio_nuevo.save()
                messages.success(request,'Anuncio Publicado')
                return redirect('product:lista')
            else:
                print("khe")
                print (form.errors)
                messages.error(request,'No se guardo')
                context ={
                    'form':form
                }
                return render(request, template_name, context)
