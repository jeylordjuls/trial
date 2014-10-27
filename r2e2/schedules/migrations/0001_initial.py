# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20141027_0654'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedules',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startTime', models.TimeField()),
                ('endTime', models.TimeField()),
                ('date', models.DateField()),
                ('event', models.ForeignKey(to='events.Events')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
