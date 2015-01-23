# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('home', '0002_auto_20141214_1829'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='requestedBy',
            field=models.ForeignKey(related_name='requests_requestedBy', blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
