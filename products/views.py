from django.views.generic import View
from django.contrib.contenttypes.models import ContentType
from .models import Anuncio, Comment, Categoria_Anuncio, SubCategoria_Anuncio,Imagen_Anuncio
from .forms import AnuncioForm, CommentForm, ImagenAnuncioForm
from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.utils.text import slugify
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib import messages
import json
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.forms import modelformset_factory, BaseFormSet, formset_factory
from django.forms.models import BaseInlineFormSet


class ListViewAnuncio(View):
    def get(self, request, categoria=None):
        template_name = "products/list_products.html"
        anuncio = Anuncio.objects.all()
        query =  request.GET.get("q")
        if query:
            anuncio = anuncio.filter(Q(titulo_anuncio__icontains=query)|
                                     Q(descripcion_anuncio__icontains=query)

                ).distinct()
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
        ImagenAnuncioFormSet = formset_factory(
            ImagenAnuncioForm,
            extra=10,
            min_num=1,
            max_num=1,
            validate_min=True

        )
        formset = ImagenAnuncioFormSet()
        context ={
            'form':form,
            'formset':formset
        }
        return render(request, template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        template_name = "products/formulario_anuncio.html"
        ImagenAnuncioFormSet = modelformset_factory(
            Imagen_Anuncio,
            form=ImagenAnuncioForm,
            fields=('imagen_anuncio',)
        )
        if request.method == 'POST':
            data = request.POST
            files = request.FILES
            print(files)
            print(data)
            form = AnuncioForm(data)
            formset = ImagenAnuncioFormSet(data)
            #print(form)
            print('B===========D')
            #print(formset)
            if form.is_valid() and formset.is_valid():
                anuncio_nuevo = form.save(commit=False)
                #formset_nuevo = formset.save(commit=False)
                print('hola')
                anuncio_nuevo.slug = slugify(anuncio_nuevo.titulo_anuncio)
                anuncio_nuevo.Moneda = request.POST.get('Moneda')
                anuncio_nuevo.vendedor = request.user
                formset_nuevo.save()
                anuncio_nuevo.save()
                messages.success(request,'Anuncio Publicado')

                for formImagen in formset.cleaned_data():
                    imagen_anuncio = formImagen['imagen']
                    photo = Imagen_Anuncio(
                        Anuncio=form,
                        imagen_anuncio=imagen_anuncio
                    )
                    photo.save()

                return redirect('product:dash')
            else:
                print("khe")
                print (form.errors)
                messages.error(request,'No se guardo')
                context ={
                    'form':form
                }
                return render(request, template_name, context)

class DetailView(View):

    def get(self,request,id,slug):
        template='products/detail.html'
        anuncio=get_object_or_404(Anuncio,id=id,slug=slug)
        initial_data = {
            "content_type": anuncio.get_content_type,
            "object_id": anuncio.id
        }
        comment_form= CommentForm(request.POST or None, initial=initial_data)
        comments=anuncio.comments
        context={
        'anuncio':anuncio,
        'comments':comments,
        'comment_form':comment_form,
        }
        return render(request,template,context)

    @method_decorator(login_required)
    def post(self,request,id,slug):
        comment_form= CommentForm(request.POST or None)
        if comment_form. is_valid():
            c_type = comment_form.cleaned_data.get("content_type")
            content_type = ContentType.objects.get(model=c_type)
            obj_id = comment_form.cleaned_data.get("object_id")
            cuerpo_data = comment_form.cleaned_data.get("cuerpo")
            parent_obj = None
            try:
                parent_id = int(request.POST.get("parent_id"))
            except:
                parent_id = None
            if parent_id:
                parent_qs = Comment.objects.filter(id = parent_id)
                if parent_qs.exists() and parent_qs.count() == 1:
                    parent_obj = parent_qs.first()

            new_comment, created = Comment.objects.get_or_create(
                                    autor = request.user,
                                    content_type= content_type,
                                    object_id= obj_id,
                                    cuerpo= cuerpo_data,
                                    parent = parent_obj,
                )
            messages.success(request,'Comentario exitoso')
        else:
            messages.error(request,'Comentario vacio')
        return redirect('product:detalle',id =id,slug=slug)

class Items(View):
    def get(self,request):
        template_name='products/item.html'
        items = Anuncio.objects.filter(vendedor= request.user)
        context = {
        'items':items,
        }
        return render(request,template_name,context)
