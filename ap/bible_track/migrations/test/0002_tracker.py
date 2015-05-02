# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '__first__'),
        ('bible_track', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='tracker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('year', models.IntegerField(default=1)),
                ('book', models.ForeignKey(to='bible_track.bible_book')),
                ('trainee', models.ForeignKey(to='accounts.Trainee')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
