<<<<<<< HEAD
from django import forms 
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']
=======
from django import forms
from.models import Post


class PostForms(forms.ModelForms):
    class Meta:
        model = Post
        fields = ['titulo', 'contenido']
>>>>>>> e5ff280 (creacion del formulario)
