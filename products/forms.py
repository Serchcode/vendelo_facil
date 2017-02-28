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
                'requiered':'true',
                'class':'validate form-control formclass'
            }
        )
    )
    descripcion_anuncio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'Describe tu anuncio aqui',
                'class':'validate form-control formclass',
                'requiered':'true',
                'class':'validate form-control formclass materialize-textarea',
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
    Moneda = forms.MultipleChoiceField(
        choices = TIPO_MONEDA,
        widget = forms.Select(
            attrs = {
                'requiered':'true',
                'class':'validate form-control formclass',
            }
        )
    )
    imagen_principal = forms.FileField(
        widget = forms.ClearableFileInput(
            attrs = {
                'class':'file-field input-field'
            }
        )
    )
    imagen_secundaria = forms.FileField(
        widget = forms.ClearableFileInput
    )
    imagen_terciaria = forms.FileField(
        widget = forms.ClearableFileInput
    )
    imagen_opcional_uno = forms.FileField(
        widget = forms.ClearableFileInput
    )
    imagen_opcional_dos = forms.FileField(
        widget = forms.ClearableFileInput
    )
    imagen_opcional_tres = forms.FileField(
        widget = forms.ClearableFileInput
    )
    categoria = forms.ModelChoiceField(
        label =u'Categoria',
        queryset = Categoria_Anuncio.objects.all(),
        widget = forms.Select(
            attrs = {
                'class':'browser-default validate form-control select input-field',
            }
        )
    )
    subcategoria_relacion = forms.ModelChoiceField(
        label =u'Especifica',
        queryset = SubCategoria_Anuncio.objects.all(),
        widget = forms.Select(
            attrs = {
                'id':'id_subcategoria_relacion',
                'class':'browser-default validate form-control select input-field',
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
            'categoria',
            'subcategoria_relacion'
        ]
    def __init__(self, *args, **kwargs):
        super(AnuncioForm, self).__init__(*args, **kwargs)
        self.fields['subcategoria_relacion'].queryset = SubCategoria_Anuncio.objects.none()
