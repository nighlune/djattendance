# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bible_track', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tracker',
            name='trainee',
            field=models.ForeignKey(to='accounts.Trainee', null=True),
        ),
    ]
