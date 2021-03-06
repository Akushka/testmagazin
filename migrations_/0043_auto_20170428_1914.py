# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-28 16:14
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteVisit', '0042_arrbought'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArrProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basket', models.IntegerField()),
                ('countProduct', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('clientName', models.CharField(max_length=200, verbose_name='Покупатель')),
            ],
        ),
        migrations.DeleteModel(
            name='ArrBought',
        ),
        migrations.AddField(
            model_name='arrproduct',
            name='Basket_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteVisit.Basket'),
        ),
    ]
