# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-25 14:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('geogermany', '0002_germangeoarea_kind_detail'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='germangeoarea',
            options={'verbose_name': 'German Geo Area', 'verbose_name_plural': 'German Geo Areas'},
        ),
    ]
