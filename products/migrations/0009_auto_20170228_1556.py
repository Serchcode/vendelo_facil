# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 21:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_auto_20170228_1554'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
