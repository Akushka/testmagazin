# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-16 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0009_auto_20170616_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_of_categories',
            name='Id_Categories',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
