# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-04 13:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0057_auto_20170504_1655'),
    ]

    operations = [
        migrations.AddField(
            model_name='basket',
            name='Basket_ip_id',
            field=models.CharField(default=0, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='basket',
            name='time_of_creation',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
