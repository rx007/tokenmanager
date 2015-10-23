# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokenmaker', '0002_auto_20151019_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='expires_datetime',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='token',
            name='issued_datetime',
            field=models.DateTimeField(),
        ),
    ]
