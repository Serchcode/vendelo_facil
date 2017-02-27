from django.http import JsonResponse
from .models import Categoria_Anuncio, SubCategoria_Anuncio


def get_subcategoria_anuncio(request):
<<<<<<< HEAD
        categoria_id = request.GET.get('categoria_id')
        print(categoria_id)
        subcategorias = SubCategoria_Anuncio.objects.none()
        options = '<option value="" selected="selected"></option>'
        if categoria_id:
            subcategorias = SubCategoria_Anuncio.objects.filter(categoria_id=categoria_id)
        for subcategoria in subcategorias:
            options += '<option value="%s">%s</option>' % (
                subcategoria.pk,
                subcategoria.nombre_subcategoria
            )
        response = {}
        response['subcategorias'] = options
        return JsonResponse(response)
=======
    categoria_id = request.GET.get('categoria_id')
    print("qye"+categoria_id)
    subcategorias = SubCategoria_Anuncio.objects.none()
    options = ''
    li = ''
    if categoria_id:
        subcategorias = SubCategoria_Anuncio.objects.filter(categoria_id=categoria_id)
    for subcategoria in subcategorias:
        li += '<li class><span>%s</span></li>' % (subcategoria.nombre_subcategoria)
        options += '<option value="%s">%s</option>' % (
            subcategoria.pk,
            subcategoria.nombre_subcategoria
        )
    response = {}
    response['subcategorias'] = options
    response['lista'] = li
    return JsonResponse(response)
>>>>>>> 1de7792f7298cce6155ced7dd6a9a979d44bb47b
