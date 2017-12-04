# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-08 11:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0004_auto_20170807_1401'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='vamdc_species_id',
            field=models.CharField(blank=True, db_index=True, max_length=27, verbose_name='VAMDC Species ID'),
        ),
    ]
