# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 19:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0013_auto_20160727_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, upload_to='posters'),
        ),
    ]
