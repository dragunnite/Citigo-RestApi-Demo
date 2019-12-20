# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-12-17 08:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='idProduct',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.FloatField(),
        ),
    ]
