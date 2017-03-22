from django.views.generic import View
from .models import Anuncio, Comment, Categoria_Anuncio, SubCategoria_Anuncio
from .forms import AnuncioForm, CommentForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils.text import slugify
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
import json
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


class ListViewAnuncio(View):
    def get(self, request, categoria=None):
        template_name = "products/list_products.html"
        anuncio = Anuncio.objects.all()
        page = request.GET.get('page', 1)
        paginator = Paginator(anuncio, 9)
        try:
            anuncios = paginator.page(page)
        except PageNotAnInteger:
            anuncios = paginator.page(1)
        except EmptyPage:
            anuncios = paginator.page(paginator.num_pages)
        tag = None
        if categoria:
            anuncios = Anuncio.objects.filter(categoria = categoria)
        context = {
            'anuncio':anuncio,
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

class DetailView(View):
<<<<<<< HEAD
    def get(self,request,id,slug):
        anuncio=get_object_or_404(Anuncio,id=id, slug=slug)
=======
    def get(self,request,slug):
>>>>>>> 9233ad73ac600f69c54287a707596f848e486d4e
        template='products/detail.html'
        anuncio=get_object_or_404(Anuncio,slug=slug)
        comentario_form=CommentForm()
        comentarios=anuncio.procoment.all()
        context={
        'anuncio':anuncio,
<<<<<<< HEAD
        }
        return render(request,template,context)
=======
        'comentario_form':comentario_form,
        'comentarios':comentarios,
        }
        print(id)
        return render(request,template,context)

    def post(self,request,slug):
        form = CommentForm(request.POST)
        anuncios = Anuncio.objects.get(slug=slug)
        com = form.save(commit=False)
        com.autor = request.user
        com.producto = anuncios
        com.save()
        return redirect('product:detalle',slug=slug)

class Items(View):
    def get(self,request):
        template_name='products/item.html'
        items = Anuncio.objects.filter(vendedor= request.user)
        context = {
        'items':items,
        }
        return render(request,template_name,context)
>>>>>>> 9233ad73ac600f69c54287a707596f848e486d4e
