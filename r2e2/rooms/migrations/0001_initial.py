# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_auto_20141027_0657'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rooms',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('roomName', models.CharField(max_length=20)),
                ('roomType', models.CharField(max_length=20)),
                ('roomNumber', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('schedules', models.ForeignKey(to='schedules.Schedules')),
            ],
            options={
                'verbose_name_plural': 'Schedules',
            },
            bases=(models.Model,),
        ),
    ]
