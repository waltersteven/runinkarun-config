# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-26 19:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partida', '0017_auto_20171126_1356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partida',
            name='speed_player',
            field=models.IntegerField(default=1),
        ),
    ]
