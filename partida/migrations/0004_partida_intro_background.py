# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-22 07:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0003_auto_20171022_0220'),
    ]

    operations = [
        migrations.AddField(
            model_name='partida',
            name='intro_background',
            field=models.CharField(choices=[('https://www-cdn.terminalfour.com/media/sky-night-stars-pexels.jpg', '1er background'), ('http://www.powerpointhintergrund.com/uploads/2017/05/simple-backgrounds-wallpaper-1920x1080--47273-24.jpeg', '2do background')], default='https://www-cdn.terminalfour.com/media/sky-night-stars-pexels.jpg', max_length=200),
        ),
    ]
