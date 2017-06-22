# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-15 18:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_on_update_cascade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='subgroup',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AlterField(
            model_name='point',
            name='count',
            field=models.BigIntegerField(null=True),
        ),
    ]