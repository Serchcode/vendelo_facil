# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 22:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20170228_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='Moneda',
            field=models.CharField(choices=[('mxn', 'MXN'), ('usd', 'USD')], max_length=5),
        ),
    ]
