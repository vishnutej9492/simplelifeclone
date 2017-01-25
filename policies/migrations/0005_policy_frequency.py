# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0004_remove_policy_frequency'),
    ]

    operations = [
        migrations.AddField(
            model_name='policy',
            name='frequency',
            field=models.CharField(max_length=20, blank=True, null=True, choices=[('monthly', 'monthly'), ('weekly', 'weekly'), ('quarterly', 'quarterly'), ('annually', 'annually')]),
        ),
    ]
