# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-28 16:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0041_auto_20170427_1847'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrBought',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.IntegerField()),
                ('countProduct', models.IntegerField()),
            ],
        ),
    ]