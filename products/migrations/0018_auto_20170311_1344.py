# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-11 19:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0017_auto_20170311_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anuncio',
            name='vendedor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productos', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='comment',
            name='producto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='procoment', to='products.Anuncio'),
        ),
    ]