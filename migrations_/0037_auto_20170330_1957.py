# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-30 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0036_auto_20170329_1735'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageinarticle',
            name='image',
        ),
        migrations.AddField(
            model_name='imageinarticle',
            name='imagePath',
            field=models.ImageField(default='', upload_to='image'),
            preserve_default=False,
        ),
    ]
