# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-20 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20181219_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='path',
            name='draft',
            field=models.BooleanField(db_column=b'brouillon', db_index=True, default=False, verbose_name='Draft'),
        ),
    ]
