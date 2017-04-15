# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-15 20:29
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_anuncio', models.CharField(max_length=200)),
                ('descripcion_anuncio', models.TextField()),
                ('precio', models.DecimalField(decimal_places=2, max_digits=10)),
                ('Moneda', models.CharField(choices=[('mxn', 'MXN'), ('usd', 'USD')], max_length=5)),
                ('fecha_anuncio', models.DateField(auto_now=True)),
                ('imagen_principal', models.ImageField(upload_to='productos/%Y/%m/%d')),
                ('imagen_secundaria', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_terciaria', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_uno', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_dos', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_tres', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_cuatro', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_cinco', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_seis', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_siete', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_ocho', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_nueve', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_diez', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_once', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('imagen_opcional_doce', models.ImageField(blank=True, null=True, upload_to='productos/%Y/%m/%d')),
                ('slug', models.SlugField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Categoria_Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_categoria', models.CharField(max_length=30)),
                ('descripcion_categoria', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('fecha_comentario', models.DateTimeField(auto_now=True)),
                ('cuerpo', models.TextField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to=settings.AUTH_USER_MODEL)),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.Comment')),
            ],
        ),
        migrations.CreateModel(
            name='SubCategoria_Anuncio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_subcategoria', models.CharField(max_length=30)),
                ('descripcion_subcategoria', models.CharField(max_length=30)),
                ('slug', models.SlugField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Categoria_Anuncio')),
            ],
        ),
        migrations.AddField(
            model_name='anuncio',
            name='categoria',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Categoria_Anuncio'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='subcategoria_relacion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.SubCategoria_Anuncio'),
        ),
        migrations.AddField(
            model_name='anuncio',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to=settings.AUTH_USER_MODEL),
        ),
    ]
