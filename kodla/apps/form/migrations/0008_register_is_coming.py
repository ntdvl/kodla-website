# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2018-04-05 11:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0007_register_is_same_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='register',
            name='is_coming',
            field=models.BooleanField(default=False, verbose_name='Coming'),
        ),
    ]
