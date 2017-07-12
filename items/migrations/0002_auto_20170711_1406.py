# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-11 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='allergen',
            name='items',
        ),
        migrations.AddField(
            model_name='item',
            name='allergens',
            field=models.ManyToManyField(to='items.Allergen'),
        ),
    ]