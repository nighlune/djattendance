from django.db import models
from accounts.models import Trainee

# Create your models here.
class Announcement(models.Model):

	TERM_CHOICES = (
		('1st', 'First Term'),
		('2nd', 'Second Term'),
		('3rd', 'Third Term'),
		('4th', 'Fourth Term'),
	)

	GENDER_CHOICES = (
		('bro', 'Brothers'),
		('sis', 'Sisters'),
	)

	TEAM_CHOICES = (
		('Ca', 'Campus'),
		('YP', 'Young People'),
		('Ch', 'Children'),
	)

	term = models.CharField(choices=TERM_CHOICES, max_length=3, blank=True)

	gender = models.CharField(choices=GENDER_CHOICES, max_length=3, blank=True)

	team = models.CharField(choices=TEAM_CHOICES, max_length=2, blank=True)

	hc = models.BooleanField(blank=True)

	couple = models.BooleanField(blank=True)

	message = models.TextField()

	date = models.DateTimeField(auto_now_add=True)


class TraineeMessage(models.Model):

	read = models.BooleanField()

	trainee = models.ForeignKey(Trainee)

	announcement = models.ForeignKey(Announcement)