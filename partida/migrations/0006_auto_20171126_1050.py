# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 15:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0005_auto_20171022_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='dificultad',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='escenario',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='intro_background',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='modo_juego',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='partida',
            name='personaje',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
