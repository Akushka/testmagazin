# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-16 09:46
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0008_auto_20170616_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='list_of_categories',
            name='categories_id',
        ),
        migrations.DeleteModel(
            name='Categories',
        ),
    ]
