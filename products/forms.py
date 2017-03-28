from django import forms
from .models import Anuncio, Categoria_Anuncio, SubCategoria_Anuncio,Comment


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
    imagen_principal = forms.FileField(
        required=True,
        widget = forms.ClearableFileInput(
        attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',

        }
    )
    )
    imagen_secundaria = forms.FileField(
        required=True,
        widget = forms.ClearableFileInput(
         attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',

        }
            )
    )
    imagen_terciaria = forms.FileField(
        required=True,
        widget = forms.ClearableFileInput(
         attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',

        }
            )
    )
    imagen_opcional_uno = forms.FileField(
        required=False,
        widget = forms.ClearableFileInput(
         attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',

        }
            )
    )
    imagen_opcional_dos = forms.FileField(
        required=False,
        widget = forms.ClearableFileInput
    )
    imagen_opcional_tres = forms.FileField(
        required=False,
        widget = forms.ClearableFileInput
    )
    categoria = forms.ModelChoiceField(
        #label =u'Categoria',
        queryset = Categoria_Anuncio.objects.all(),
        widget = forms.Select,
    )
    subcategoria_relacion = forms.ModelChoiceField(
        #label =u'Subcategoria',
        queryset = SubCategoria_Anuncio.objects.all(),
        widget = forms.Select,
    )


    class Meta:
        model = Anuncio
        fields = [
            'titulo_anuncio',
            'descripcion_anuncio',
            'precio',
            'categoria',
            'subcategoria_relacion',
            'imagen_principal',
            'imagen_secundaria',
            'imagen_terciaria',
            'imagen_opcional_uno'
        ]

    def __init__(self, *args, **kwargs):
        super(AnuncioForm, self).__init__(*args, **kwargs)
        self.fields['subcategoria_relacion'].queryset = SubCategoria_Anuncio.objects.all()

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['cuerpo']
        labels  = {
            'cuerpo':'Preguntas al vendedor:'
        }

