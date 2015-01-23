# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_requests_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='user_type',
        ),
    ]
