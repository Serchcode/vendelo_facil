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
                'placeholder':'',
                'class':'validate form-control formclass',
                'label':'Titulo del Anuncio',
                'requiered':'true',
            }
        )
    )
    descripcion_anuncio = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'placeholder':'',
                'class':'validate form-control formclass materialize-textarea',
                'requiered':'true',
            }
        )
    )
    precio = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'placeholder':'',
                'class':'validate form-control',
                'requiered':'true',
            }
        )
    )
    Moneda = forms.MultipleChoiceField(
        choices = TIPO_MONEDA,
        widget = forms.Select,
    )
    imagen_principal = forms.FileField(
        widget = forms.ClearableFileInput(
        attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',

        }
    )
    )
    imagen_secundaria = forms.FileField(
        widget = forms.ClearableFileInput(
         attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',

        }    
            )
    )
    imagen_terciaria = forms.FileField(
        widget = forms.ClearableFileInput(
         attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',

        }    
            )
    )
    imagen_opcional_uno = forms.FileField(
        widget = forms.ClearableFileInput(
         attrs={
                'class': 'waves-effect waves-light btn #43a047 green darken-1',
                'type': 'file',

        }        
            )
    )
    imagen_opcional_dos = forms.FileField(
        widget = forms.ClearableFileInput
    )
    imagen_opcional_tres = forms.FileField(
        widget = forms.ClearableFileInput
    )
    categoria = forms.ModelChoiceField(
        #label =u'Categoria',       
        queryset = Categoria_Anuncio.objects.all(),
        widget = forms.Select,
        required =True,
    )
    subcategoria_relacion = forms.ModelChoiceField(
        #label =u'Subcategoria',
        queryset = SubCategoria_Anuncio.objects.all(),
        widget = forms.Select,
        required=True,         
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
