# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import policies.models
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0005_policy_frequency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='pdf',
            field=models.FileField(upload_to=policies.models.file_name, storage=django.core.files.storage.FileSystemStorage(location='/media'), null=True, blank=True),
        ),
    ]
