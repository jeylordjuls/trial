# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=30, null=True, blank=True)),
                ('eventType', models.CharField(max_length=30, null=True, blank=True)),
                ('startTime', models.TimeField(null=True, blank=True)),
                ('endTime', models.TimeField(null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
            ],
            options={
                'verbose_name_plural': 'Requests',
            },
            bases=(models.Model,),
        ),
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
        migrations.AddField(
            model_name='requests',
            name='room',
            field=models.ForeignKey(to='home.Rooms'),
            preserve_default=True,
        ),
    ]
