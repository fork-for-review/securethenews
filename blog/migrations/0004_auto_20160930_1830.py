# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-30 18:30
from __future__ import unicode_literals

from django.db import migrations
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogindexpage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=wagtail.wagtailcore.fields.StreamField((('heading', wagtail.wagtailcore.blocks.CharBlock()), ('rich_text', wagtail.wagtailcore.blocks.RichTextBlock()), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()))),
        ),
    ]
