# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0004_auto_20150526_0535'),
    ]

    operations = [
        migrations.AlterField(
            model_name='managelog',
            name='log_time',
            field=models.DateTimeField(),
            preserve_default=True,
        ),
    ]
