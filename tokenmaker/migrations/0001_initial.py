# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('token', models.CharField(max_length=36)),
                ('token_previous', models.CharField(max_length=36, blank=True, null=True)),
                ('create_datetime', models.DateTimeField(auto_now=True)),
                ('updated_datetime', models.DateTimeField(auto_now_add=True)),
                ('by_user', models.CharField(max_length=40)),
                ('status', models.IntegerField(default=0, choices=[(0, 'avaliable'), (1, 'not avaliable')])),
            ],
        ),
    ]
