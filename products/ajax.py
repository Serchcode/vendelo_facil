from django.http import JsonResponse
from .models import Categoria_Anuncio, SubCategoria_Anuncio
from django.shortcuts import render

def get_subcategoria_anuncio(request):
    categoria_id = request.GET.get('categoria_id')
    print(categoria_id)
    subcategorias = SubCategoria_Anuncio.objects.none()
    options = ''
    if categoria_id:
        subcategorias = SubCategoria_Anuncio.objects.filter(categoria_id=categoria_id)
    for subcategoria in subcategorias:
        options += '<option value="%s">%s</option>' % (
            subcategoria.pk,
            subcategoria.nombre_subcategoria
        )
    print(options)
    response = {}
    response['subcategorias'] = options
    print(response)
    return JsonResponse(response)
