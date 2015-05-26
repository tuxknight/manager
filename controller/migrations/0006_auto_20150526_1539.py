# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0005_auto_20150526_0627'),
    ]

    operations = [
        migrations.AlterField(
            model_name='device',
            name='id',
            field=models.IntegerField(serialize=False, auto_created=True, primary_key=True),
            preserve_default=True,
        ),
    ]
