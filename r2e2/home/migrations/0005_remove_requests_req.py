# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_requests_req'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requests',
            name='req',
        ),
    ]
