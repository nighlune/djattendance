# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('absent_trainee_roster', '0001_initial'),
        ('houses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='roster',
            name='unreported_houses',
            field=models.ManyToManyField(related_name='rosters', to='houses.House', blank=True),
        ),
        migrations.AddField(
            model_name='entry',
            name='absentee',
            field=models.ForeignKey(to='absent_trainee_roster.Absentee'),
        ),
        migrations.AddField(
            model_name='entry',
            name='roster',
            field=models.ForeignKey(to='absent_trainee_roster.Roster'),
        ),
        migrations.AddField(
            model_name='absentee',
            name='account',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
