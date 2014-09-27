import datetime

from django.db import models
from accounts.models import Trainee
from classes.models import Class

from exams.utils import time_in_range


""" exams models.py

This module allows TA's to create, read, update, and delete exams, and view exam statistics, 
and for trainees to take exams.

DATA MODELS:
	- ExamTemplate: the exam created by the TA for a class.
	- Exam: a specific instance of an exam template, linked to a trainees
		consists of responses
	- Question (abstract): the question prompts which belong to an exam template 
	- Response (abstract): a trainee's response to a question prompt, belonging to an exam.
		- TextQuestion
		- TextResponse

"""

class ExamTemplate(models.Model):
	created = models.DateTimeField(auto_now_add=True)

	# note: class includes term
	training_class = models.ForeignKey(Class)

	# an exam is available to be taken by trainees during a given span of time
	opens_on = models.DateTimeField(auto_now=False)
	closes_on = models.DateTimeField(auto_now=False)

	# cut-off percentage; generally 60% but manually definable by TAs
	cutoff = models.IntegerField(default=60)

	def __unicode__(self):
		return "Exam for %s, [%s]" % (self.training_class, self.training_class.term)

	def _exams(self):
		return 0
	exams = property(_exams)

	def _is_open(self):
		return time_in_range(self.opens_on, self.closes_on, datetime.datetime.now())
	is_open = property(_is_open)


class Exam(ExamTemplate):
	is_complete = models.BooleanField(default=False)
	is_graded = models.BooleanField(default=False)
	grade = models.IntegerField(default=0)

	# each exam instance is linked to exactly one trainee
	trainee = models.ForeignKey(Trainee)

	def __unicode__(self):
		return "%s's exam" % (self.trainee)


""" The Question and Response classes are abstract so different types of questions
and their corresponding response types can be easily created, i.e.,
MultipleChoiceQuestion, MultipleChoiceResponse, BooleanQuestion, etc. """

class Question(models.Model):
	exam_template = models.ForeignKey(ExamTemplate, related_name="questions")

	class Meta:
		abstract = True

class Response(models.Model):
	exam = models.ForeignKey(Exam, related_name="responses")

	class Meta:
		abstract = True

class TextQuestion(Question):
	body = models.CharField(max_length=500)

class TextResponse(Response):
	body = models.CharField(max_length=500)


