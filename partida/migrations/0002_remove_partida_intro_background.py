# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 07:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='partida',
            name='intro_background',
        ),
    ]
