# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 09:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0002_videos'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Videos',
        ),
    ]
