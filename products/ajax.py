from django.http import JsonResponse
from .models import Categoria_Anuncio, SubCategoria_Anuncio


def get_subcategoria_anuncio(request):
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