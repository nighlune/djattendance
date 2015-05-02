from django.db import models
from accounts.models import Trainee

""" bible_track models.py
The bible_track module is used to track a trainee's Bible reading
progress throughout the 4 terms. 

DATA MODELS:
    - bible_book: a class that is used to store the books from the Bible
    and the content of those books (name, verses, chapters). 

    - tracker: a class that contains the bible books a trainee has
    completed and what year (1st or 2nd year) the book was completed. 

"""

class bible_book(models.Model):

	BIBLE_BOOKS = (
        ('GEN', 'Genesis'),
        ('EXO', 'Exodus'),
        ('LEV', 'Leviticus'),
        ('NUM', 'Numbers'),
        ('DEUT', 'Deuteronomy'),
        ('JOSH', 'Joshua'),
        ('JUDGE', 'Judges'),
        ('RUTH', 'Ruth'),
        ('1SAM', '1 Samuel'),
        ('2SAM', '2 Samuel'),
        ('1KINGS', '1 Kings'),
        ('2KINGS', '2 Kings'),
        ('1CHRON', '1 Chronicles'),
        ('2CHRON', '2 Chronicles'),
        ('EZRA', 'Ezra'),
        ('NEH', 'Nehemiah'),
        ('ESTH', 'Esther'),
        ('JOB', 'Job'),
        ('PSA', 'Psalms'),
        ('PROV', 'Proverbs'),
        ('ECCL', 'Ecclesiastes'),
        ('SS', 'Song of Songs'),
        ('ISA', 'Isaiah'),
        ('JER', 'Jeremiah'),
        ('LAM', 'Lamentations'),
        ('EZEK', 'Ezekiel'),
        ('DAN', 'Daniel'),
        ('HOSEA', 'Hosea'),
        ('JOEL', 'Joel'),
        ('AMOS', 'Amos'),
        ('OBAD', 'Obadiah'),
        ('JONAH', 'Jonah'),
        ('MICAH', 'Micah'),
        ('NAHUM', 'Nahum'),
        ('HAB', 'Habakkuk'),
        ('ZEPH', 'Zephaniah'),
        ('HAG', 'Haggai'),
        ('ZECH', 'Zechariah'),
        ('MAL', 'Malachi'),
        ('MATT', 'Matthew'),
        ('MARK', 'Mark'),
        ('LUKE', 'Luke'),
        ('JOHN', 'John'),
        ('ACTS', 'Acts'),
        ('ROM', 'Romans'),
        ('1COR', '1 Corinthians'),
        ('2COR', '2 Corinthians'),
        ('GAL', 'Galatians'),
        ('EPH', 'Ephesians'),
        ('PHIL', 'Philippians'),
        ('COL', 'Colossians'),
        ('1THES', '1 Thessalonians'),
        ('2THES', '2 Thessalonians'),
        ('1TIM', '1 Timothy'),
        ('2TIM', '2 Timothy'),
        ('TITUS', 'Titus'),
        ('PHILEM', 'Philemon'),
        ('HEB', 'Hebrews'),
        ('JAMES', 'James'),
        ('1PET', '1 Peter'),
        ('2PET', '2 Peter'),
        ('1JOHN', '1 John'),
        ('2JOHN', '2 John'),
        ('3JOHN', '3 John'),
        ('JUDE', 'Jude'),
        ('REV', 'Revelation'),
    )
     
	name = models.CharField(max_length=6, choices=BIBLE_BOOKS)
	verses = models.IntegerField(default=0)
	chapters = models.IntegerField(default=0)
	
	def __str__(self):
		return self.name;
		
	def toString(self):
		return self.get_name_display();	

class tracker(models.Model):
	trainee = models.ForeignKey(Trainee, null=True)
	book = models.ForeignKey(bible_book)
	year = models.IntegerField(default=1)
	
	def __str__(self):
		return self.book.name;

