# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0006_auto_20170125_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='image_name',
            field=models.CharField(max_length=100),
        ),
    ]
