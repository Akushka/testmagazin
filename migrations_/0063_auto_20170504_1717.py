# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-04 14:17
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0062_basket_time_of_creation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='time_of_creation',
        ),
        migrations.AddField(
            model_name='basket',
            name='intime',
            field=models.TimeField(default=datetime.time(0, 0), verbose_name='IN-TIME'),
        ),
    ]
