# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requests',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=30, null=True, blank=True)),
                ('partiNumber', models.IntegerField(null=True, blank=True)),
                ('startTime', models.TimeField(null=True, blank=True)),
                ('endTime', models.TimeField(null=True, blank=True)),
                ('date', models.DateField(null=True, blank=True)),
                ('purpose', models.CharField(max_length=50, null=True, blank=True)),
                ('tag', models.IntegerField(null=True, blank=True)),
                ('approvedBy', models.ForeignKey(related_name='requests_adminApproved', blank=True, to='users.UserProfile', null=True)),
                ('requestedBy', models.ForeignKey(related_name='requests_requestedBy', blank=True, to='users.UserProfile', null=True)),
                ('room', models.ForeignKey(to='rooms.Rooms')),
            ],
            options={
                'verbose_name_plural': 'Requests',
            },
            bases=(models.Model,),
        ),
    ]
