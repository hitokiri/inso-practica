from django.forms import ModelForm
from .models import Articulo



class FormHome(ModelForm):
    class Meta:
        model = Articulo
        exclude = 'id',

