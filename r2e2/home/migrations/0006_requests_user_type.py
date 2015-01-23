# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('home', '0005_remove_requests_req'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='user_type',
            field=models.ForeignKey(blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
