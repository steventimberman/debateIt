# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-26 19:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('debate', '0020_remove_point_debate_side'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debatetopic',
            name='article_URL',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='debatetopic',
            name='cover_photo',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
