# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-22 01:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0018_auto_20170311_1344'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(auto_now=True)),
                ('cuerpo', models.TextField()),
                ('replied', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta', to=settings.AUTH_USER_MODEL)),
                ('respuesta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='respuesta_coment', to='products.Comment')),
            ],
        ),
    ]