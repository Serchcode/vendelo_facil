# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-27 20:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='imagen_principal',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagen_secundaria',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
        migrations.AlterField(
            model_name='anuncio',
            name='imagen_terciaria',
            field=models.ImageField(blank=True, null=True, upload_to='productos'),
        ),
    ]