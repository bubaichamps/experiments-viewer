# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-21 22:06
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_observations', models.IntegerField()),
                ('population', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CategoryPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket', models.CharField(max_length=255)),
                ('proportion', models.FloatField()),
                ('rank', models.IntegerField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_points', to='api.CategoryCollection')),
            ],
        ),
        migrations.CreateModel(
            name='LogCollection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_observations', models.IntegerField()),
                ('population', models.CharField(max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='LogPoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bucket', models.FloatField()),
                ('proportion', models.FloatField()),
                ('collection', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='_points', to='api.LogCollection')),
            ],
        ),
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('metadata', django.contrib.postgres.fields.jsonb.JSONField()),
            ],
        ),
        migrations.AddField(
            model_name='logcollection',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Metric'),
        ),
        migrations.AddField(
            model_name='categorycollection',
            name='metric',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Metric'),
        ),
    ]
