# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-08-17 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articulo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('description', models.TextField()),
                ('fecha_de_nacimiento', models.DateField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('modify', models.DateTimeField(auto_now=True)),
                ('img', models.ImageField(upload_to='imagenes')),
                ('archivo', models.FileField(upload_to='archivos')),
            ],
            options={
                'verbose_name': 'Articulo',
                'verbose_name_plural': 'Articulos',
            },
        ),
    ]
