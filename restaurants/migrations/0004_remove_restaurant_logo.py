# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-12 12:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_restaurant_logo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='logo',
        ),
    ]
