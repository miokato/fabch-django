# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 09:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0006_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='string',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
