# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-06-21 11:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0018_remove_listofcategories_action_categories'),
    ]

    operations = [
        migrations.AddField(
            model_name='imageinarticle',
            name='imageUrlArticle',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
