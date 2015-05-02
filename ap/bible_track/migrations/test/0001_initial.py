# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bible_book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=6, choices=[(b'GEN', b'Genesis'), (b'EXO', b'Exodus'), (b'LEV', b'Leviticus'), (b'NUM', b'Numbers'), (b'DEUT', b'Deuteronomy'), (b'JOSH', b'Joshua'), (b'JUDGE', b'Judges'), (b'RUTH', b'Ruth'), (b'1SAM', b'1 Samuel'), (b'2SAM', b'2 Samuel'), (b'1KINGS', b'1 Kings'), (b'2KINGS', b'2 Kings'), (b'1CHRON', b'1 Chronicles'), (b'2CHRON', b'2 Chronicles'), (b'EZRA', b'Ezra'), (b'NEH', b'Nehemiah'), (b'ESTH', b'Esther'), (b'JOB', b'Job'), (b'PSA', b'Psalms'), (b'PROV', b'Proverbs'), (b'ECCL', b'Ecclesiastes'), (b'SS', b'Song of Songs'), (b'ISA', b'Isaiah'), (b'JER', b'Jeremiah'), (b'LAM', b'Lamentations'), (b'EZEK', b'Ezekiel'), (b'DAN', b'Daniel'), (b'HOSEA', b'Hosea'), (b'JOEL', b'Joel'), (b'AMOS', b'Amos'), (b'OBAD', b'Obadiah'), (b'JONAH', b'Jonah'), (b'MICAH', b'Micah'), (b'NAHUM', b'Nahum'), (b'HAB', b'Habakkuk'), (b'ZEPH', b'Zephaniah'), (b'HAG', b'Haggai'), (b'ZECH', b'Zechariah'), (b'MAL', b'Malachi'), (b'MATT', b'Matthew'), (b'MARK', b'Mark'), (b'LUKE', b'Luke'), (b'JOHN', b'John'), (b'ACTS', b'Acts'), (b'ROM', b'Romans'), (b'1COR', b'1 Corinthians'), (b'2COR', b'2 Corinthians'), (b'GAL', b'Galatians'), (b'EPH', b'Ephesians'), (b'PHIL', b'Philippians'), (b'COL', b'Colossians'), (b'1THES', b'1 Thessalonians'), (b'2THES', b'2 Thessalonians'), (b'1TIM', b'1 Timothy'), (b'2TIM', b'2 Timothy'), (b'TITUS', b'Titus'), (b'PHILEM', b'Philemon'), (b'HEB', b'Hebrews'), (b'JAMES', b'James'), (b'1PET', b'1 Peter'), (b'2PET', b'2 Peter'), (b'1JOHN', b'1 John'), (b'2JOHN', b'2 John'), (b'3JOHN', b'3 John'), (b'JUDE', b'Jude'), (b'REV', b'Revelation')])),
                ('verves', models.IntegerField(default=0)),
                ('chapters', models.IntegerField(default=0)),
                ('completed', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
