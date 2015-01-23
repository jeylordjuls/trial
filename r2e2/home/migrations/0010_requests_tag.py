# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_auto_20150121_0202'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='tag',
            field=models.IntegerField(null=True, blank=True),
            preserve_default=True,
        ),
    ]
