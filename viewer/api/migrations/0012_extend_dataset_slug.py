# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-19 22:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_dataset_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='slug',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]