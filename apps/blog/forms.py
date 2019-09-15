from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Post, Categoria, PQR


class EditPostForm(forms.ModelForm):

    class Meta:
        model = Post

        fields = [
          'titulo',
          'descripcion',
          'contenido',
          'categoria'
        ]

        labels = {
          'titulo': 'Titulo',
          'descripcion': 'Descripción',
          'contenido': 'Contenido',
          'categoria': 'Categoria'
        }

        widgets = {
          'titulo': forms.TextInput(attrs={ 'class': 'input' }),
          'descripcion': forms.TextInput(attrs={ 'class': 'input' }),
          'contenido': forms.CharField(widget=CKEditorWidget()),
          'cetegoria': forms.CharField(widget=forms.Select(choices=Categoria.objects.all()))
        }


class PQRForm(forms.ModelForm):
    
    class Meta:
        model = PQR

        fields = (
            'nombres',
            'apellidos',
            'email',
            'asunto',
            'mensaje'
        )