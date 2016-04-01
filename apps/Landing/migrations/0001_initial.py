# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-01 01:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=100)),
                ('interest', models.TextField(max_length=200)),
                ('favo_language', models.TextField(max_length=200)),
            ],
            options={
                'db_table': 'person',
            },
        ),
    ]
