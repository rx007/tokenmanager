# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tokenmaker', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='token',
            old_name='updated_datetime',
            new_name='expires_datetime',
        ),
        migrations.RenameField(
            model_name='token',
            old_name='create_datetime',
            new_name='issued_datetime',
        ),
    ]
