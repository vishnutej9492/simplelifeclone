# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('policies', '0009_auto_20170125_2306'),
    ]

    operations = [
        migrations.AlterField(
            model_name='policy',
            name='frequency',
            field=models.CharField(max_length=20, blank=True, null=True, choices=[('monthly', 'Monthly'), ('weekly', 'Weekly'), ('quarterly', 'Quarterly'), ('annually', 'Annually')]),
        ),
        migrations.AlterField(
            model_name='policy',
            name='image_name',
            field=models.CharField(max_length=100, blank=True, null=True, choices=[('auto', 'Auto'), ('umbrella', 'Umbrella'), ('workers', 'Workers comp'), ('aircraft', 'Aircraft'), ('boat', 'Boat'), ('pet', 'Pet'), ('renters', 'Renters'), ('home owners', 'Home owners')]),
        ),
    ]
