from django import forms
from .models import Anuncio, Categoria_Anuncio, SubCategoria_Anuncio,Comment, Imagen_Anuncio


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
            'imagen_relacion'
        ]

    def __init__(self, *args, **kwargs):
        super(AnuncioForm, self).__init__(*args, **kwargs)
        self.fields['subcategoria_relacion'].queryset = SubCategoria_Anuncio.objects.all()

class CommentForm(forms.Form):
    content_type = forms.CharField(widget=forms.HiddenInput)
    object_id = forms.CharField(widget=forms.HiddenInput)
    #parent_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    cuerpo = forms.CharField(label= 'Comentar', widget=forms.Textarea)

class ImagenAnuncioForm(forms.Form):
    imagen_anuncio = forms.FileField(
        required=True,
        widget = forms.ClearableFileInput(
        attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',
                'multiple':'',

        }
    )
    )
    class Meta:
        model = Imagen_Anuncio
        field = ['imagen_anuncio',]
