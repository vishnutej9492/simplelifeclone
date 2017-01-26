# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0008_auto_20170125_2208'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='policy',
            name='image_name',
            field=models.CharField(max_length=100, blank=True, null=True, choices=[('test1', 'test1'), ('test2', 'test2'), ('test3', 'test3')]),
        ),
        migrations.AlterField(
            model_name='policy',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
