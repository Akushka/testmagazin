# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-04 14:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0061_sitename_created_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='time_of_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
