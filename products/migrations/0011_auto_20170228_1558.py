# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-28 21:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0010_auto_20170228_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='precio',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
