# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import policies.models


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0007_auto_20170125_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='pdf',
            field=models.FileField(blank=True, null=True, upload_to=policies.models.file_name),
        ),
    ]
