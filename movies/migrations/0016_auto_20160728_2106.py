# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 00:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0015_auto_20160728_0152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=models.ImageField(blank=True, default='/movies/static/movies/poster_not_available.jpg', upload_to='posters'),
        ),
    ]
