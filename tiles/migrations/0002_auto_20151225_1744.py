# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-25 17:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tile',
            name='public',
            field=models.BooleanField(default='false'),
        ),
        migrations.AddField(
            model_name='tile',
            name='solved',
            field=models.BooleanField(default='false'),
        ),
        migrations.AddField(
            model_name='user',
            name='score',
            field=models.IntegerField(default=0),
        ),
    ]
