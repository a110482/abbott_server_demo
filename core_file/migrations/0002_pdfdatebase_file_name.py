# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-29 06:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core_file', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfdatebase',
            name='file_name',
            field=models.TextField(blank=True),
        ),
    ]