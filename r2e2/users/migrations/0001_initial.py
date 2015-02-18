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
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('userType', models.CharField(default=b'SA', max_length=20, choices=[(b'Organization', b'Organization'), (b'Faculty', b'Faculty'), (b'Guest', b'Guest'), (b'System Administrator', b'System Admin'), (b'Building Administrator', b'Building Admin'), (b'Deparment Chair', b'Dept Chair')])),
                ('priorityLevel', models.IntegerField(default=0)),
                ('additionalProperties', models.CharField(max_length=40)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
