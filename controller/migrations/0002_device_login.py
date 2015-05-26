# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('controller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='login',
            field=models.CharField(default=b'root', max_length=15),
            preserve_default=True,
        ),
    ]
