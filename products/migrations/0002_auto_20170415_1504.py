# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-15 20:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='anuncio',
            old_name='imagen_opcional_dos',
            new_name='imagen_opcional_doss',
        ),
    ]
