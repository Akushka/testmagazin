# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-20 11:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0015_auto_20170616_1403'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofcategories',
            name='action_categories',
            field=models.BooleanField(default=False),
        ),
    ]