# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='frequency',
            field=models.CharField(max_length=20, blank=True, choices=[('monthly', 'monthly'), ('weekly', 'weekly'), ('quarterly', 'quarterly'), ('annually', 'annually')], null=True),
        ),
    ]
