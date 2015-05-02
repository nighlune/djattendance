# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible_track', '0002_tracker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bible_book',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='bible_book',
            name='verves',
        ),
    ]
