# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_requests_approved_by'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requests',
            old_name='approved_By',
            new_name='approvedBy',
        ),
    ]
