# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 19:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20170227_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='Moneda',
            field=models.CharField(choices=[('mxn', 'MXN'), ('usd', 'USD')], default='Moneda de cambio', max_length=5),
        ),
    ]
