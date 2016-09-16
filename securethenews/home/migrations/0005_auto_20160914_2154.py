# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-09-14 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_contentpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentpage',
            name='button_text',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='contentpage',
            name='button_url',
            field=models.CharField(default='', max_length=255),
        ),
    ]
