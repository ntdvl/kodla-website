# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-03-01 09:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SocialAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='Create Date')),
                ('update_date', models.DateTimeField(auto_now=True, verbose_name='Update Date')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Name')),
                ('style_id', models.CharField(blank=True, max_length=100, null=True, verbose_name='Style Id')),
                ('style_class', models.CharField(blank=True, max_length=100, null=True, verbose_name='Style Class')),
            ],
            options={
                'verbose_name': 'Social Accounts',
                'ordering': ('name',),
            },
        ),
    ]
