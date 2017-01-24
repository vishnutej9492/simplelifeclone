# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0002_auto_20170116_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='image_name',
            field=models.CharField(verbose_name="person's first name", max_length=100, default=datetime.datetime(2017, 1, 24, 5, 23, 8, 995371, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='policy',
            unique_together=set([]),
        ),
    ]
