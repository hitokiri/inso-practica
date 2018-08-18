# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import FormHome
from .models import Articulo
# Create your views here.

def home(request):
    form = FormHome()
    articulos = Articulo.objects.all()
    ctx = {'form': form, 'articulos': articulos}
    return render(request,'main/home.html', ctx)