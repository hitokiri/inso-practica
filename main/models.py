# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField('nombre', max_length=50)
    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"

    def __str__(self):
        return self.name + 'lol'


class Articulo(models.Model):
    tags = models.ManyToManyField('Tag')
    name = models.CharField('nombre', max_length=50)
    description = models.TextField()
    fecha_de_nacimiento = models.DateField()
    create_at = models.DateTimeField(auto_now_add=True)
    modify = models.DateTimeField(auto_now=True)
    img = models.ImageField(upload_to='imagenes', blank=True)
    archivo = models.FileField(upload_to='archivos', blank=True)
    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.name

