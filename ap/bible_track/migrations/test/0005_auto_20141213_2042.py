# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible_track', '0004_bible_book_verses'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tracker',
            name='book',
        ),
        migrations.DeleteModel(
            name='bible_book',
        ),
        migrations.RemoveField(
            model_name='tracker',
            name='trainee',
        ),
        migrations.DeleteModel(
            name='tracker',
        ),
    ]
