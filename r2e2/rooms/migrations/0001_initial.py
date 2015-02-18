# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roomName', models.CharField(max_length=20)),
                ('roomType', models.CharField(max_length=20)),
                ('roomNumber', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Rooms',
            },
            bases=(models.Model,),
        ),
    ]
