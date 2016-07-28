# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-27 18:31
from __future__ import unicode_literals

from django.db import migrations, models
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0008_auto_20160727_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='poster',
            field=sorl.thumbnail.fields.ImageField(upload_to=models.CharField(max_length=200)),
        ),
    ]