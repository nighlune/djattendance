# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible_track', '0003_auto_20141213_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='bible_book',
            name='verses',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
