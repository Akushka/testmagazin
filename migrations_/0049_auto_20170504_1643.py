# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-05-04 13:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0048_basket_time_of_creation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basket',
            name='time_of_creation',
            field=models.DateTimeField(),
        ),
    ]
