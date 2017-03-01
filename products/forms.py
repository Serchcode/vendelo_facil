from django import forms
from .models import Anuncio, Categoria_Anuncio, SubCategoria_Anuncio


TIPO_MONEDA =(
    ('selec','Selecciona una Moneda'),
    ('mxn','MXN'),
    ('usd','USD')
)

class AnuncioForm(forms.ModelForm):
    Moneda = forms.ChoiceField(
        choices=TIPO_MONEDA,
        required=True,
        widget = forms.Select,

    )
    categoria = forms.ModelChoiceField(
        #label =u'Categoria',
        queryset = Categoria_Anuncio.objects.all(),
        widget = forms.Select,
        required =False,
    )
    subcategoria_relacion = forms.ModelChoiceField(
        #label =u'Subcategoria',
        queryset = SubCategoria_Anuncio.objects.all(),
        widget = forms.Select,
        required=False,
    )


    class Meta:
        model = Anuncio
        fields = [
            'titulo_anuncio',
            'descripcion_anuncio',
            'precio',
            'subcategoria_relacion',
            'imagen_principal',
            'imagen_secundaria',
            'imagen_terciaria',
            'imagen_opcional_uno'
        ]

    def __init__(self, *args, **kwargs):
        super(AnuncioForm, self).__init__(*args, **kwargs)
        self.fields['subcategoria_relacion'].queryset = SubCategoria_Anuncio.objects.none()
