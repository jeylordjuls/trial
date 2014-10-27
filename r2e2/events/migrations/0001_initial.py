# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('eventName', models.CharField(max_length=30)),
                ('eventType', models.CharField(max_length=20)),
                ('timeStamp', models.DateField()),
                ('approvalStatus', models.CharField(max_length=30)),
                ('approved_by', models.ForeignKey(related_name='events_approved_by', to=settings.AUTH_USER_MODEL)),
                ('created_by', models.ForeignKey(related_name='events_created_by', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
