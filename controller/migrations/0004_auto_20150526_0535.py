# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0003_modules'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='notes',
            field=models.CharField(max_length=5000, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='modules',
            name='keys',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='modules',
            name='values',
            field=models.CharField(max_length=10, blank=True),
            preserve_default=True,
        ),
    ]
