# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='schedules',
            options={'verbose_name_plural': 'Schedules'},
        ),
    ]
