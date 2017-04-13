from django.shortcuts import render,redirect
from django.views.generic import View
from products.models import Anuncio

class HomeView(View):
	def get(self, request):
		template_name="index.html"
		return render(request,template_name)

class ListViewAnuncio(View):
    def get(self, request, categoria=None):
        template_name = "products/list_products.html"
        anuncio = Anuncio.objects.all()
        query =  request.GET.get("q")
        if query:
            anuncio = anuncio.filter(Q(titulo_anuncio__icontains=query)|
                                     Q(descripcion_anuncio__icontains=query)

                ).distinct()
        context = {
            'anuncio':anuncio,
            'anuncios':anuncios,
        }
        return render(request,template_name,context)