from django import forms
from .models import Anuncio, Categoria_Anuncio, SubCategoria_Anuncio


TIPO_MONEDA =(
    ('mxn','MXN'),
    ('usd','USD')
)

class AnuncioForm(forms.ModelForm):
    titulo_anuncio = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'placeholder':'Escribe le titulo de tu anuncio aqui',
                'class':'validate form-control formclass',
                'label':'Titulo del Anuncio',
                'requiered':'true'
            }
        )
    )
    descripcion_anuncio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'Describe tu anuncio aqui',
                'class':'validate form-control formclass',
                'requiered':'true',
            }
        )
    )
    precio = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Valor monetario de tu articulo',
                'class':'validate form-control formclass',
                'requiered':'true',
            }
        )
    )

    class Meta:
        model = Anuncio
        fields = [
            'titulo_anuncio',
            'descripcion_anuncio',
            'precio',
            'Moneda',
            'imagen_principal',
            'imagen_secundaria',
            'imagen_terciaria',
            'imagen_opcional_uno',
            'categoria'
        ]
