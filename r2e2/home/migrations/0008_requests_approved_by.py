# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('home', '0007_remove_requests_user_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='requests',
            name='approved_By',
            field=models.ForeignKey(related_name='requests_adminApproved', blank=True, to='accounts.UserProfile', null=True),
            preserve_default=True,
        ),
    ]
