from django.db import models
from terms.models import Term


""" SCHEDULES models.py

This schedules module is for representing weekly trainee schedules.

Data Models
- Event:
    an event, such as class or study time, that trainees need to attend.
- EventGroup:

- Schedule:
    a collection of events for one trainee. each trainee should have one
    schedule per term.
- ScheduleTemplate:
    a generic collection of events for one week that can be applied to a
    trainee or group of trainees.

"""


class Event(models.Model):

    EVENT_TYPES = (
        ('C', 'Class'),
        ('S', 'Study'),
        ('M', 'Meal'),
        ('H', 'House'),
        ('T', 'Team'),
        ('L', 'Church Meeting'),  # C is taken, so L for locality
        ('*', 'Special'),  # S is taken, so * for special
    )

    MONITOR_TYPES = (
        ('AM', 'Attendance Monitor'),
        ('TM', 'Team Monitor'),
        ('HC', 'House Coordinator'),
    )

    # name of event, e.g. Full Ministry of Christ, or Lights Out
    name = models.CharField(max_length=30)

    # the event's shortcode, e.g. FMoC or Lights
    shortcode = models.CharField(max_length=10)

    # a description of the event (optional)
    description = models.CharField(max_length=250, blank=True)

    # a groupID. used to group repeating events
    group = models.ForeignKey(EventGroup)

    # the type of event
    type = models.CharField(max_length=1, choice=EVENT_TYPES)

    # who takes roll for this event
    monitor = models.CharField(max_length=2, choice=MONITOR_TYPES)

    # which term this event is active in
    term = models.ForeignKey(Term)

    # weeks 0-19 for the 20 weeks of the training
    week = models.PositiveSmallIntegerField()

    # days 0-6 (LD through Saturday)
    day = models.PositiveSmallIntegerField()

    start = models.TimeField()

    end = models.TimeField()

    def _startDate(self):
        return self.term.getDate(0, 0)
    startDate = property(_startDate)

    def _endDate(self):
        return self.term.getDate(19, 6)
    endDate = property(_endDate)


class EventGroup(models.Model):

    # for now, this should just be the same as the event name
    name = models.CharField(max_length=30)

    # which days this event repeats on, starting with Monday (0) through LD (6)
    # i.e. an event that repeats on Tuesday and Thursday would be (1,3)
    repeat = models.CommaSeparatedIntegerField(max_length=7)

    # override save(): ensure all events in eventgroup are also deleted
    def save(self, *args, **kwargs):
        Events.objects.filter(eventgroup=self.id).delete()
        super(EventGroup, self).save(*args, **kwargs)


class Schedule(models.Model):

    # which trainee this schedule belongs to
    'trainee = models.ForeignKey()  # TODO: write and import user model

    # which term this schedule applies to
    term = models.ForeignKey(Term)

    # which events are on this schedule
    events = models.ManyToManyField(Event)

    def clear(startDate, endDate, self):
        # delete events within this interval on this schedule
        Event.objects.filter(schedule=self.id).filter(startDate__gte=startDate).filter(endDate__lte=endDate).delete()

    def clear(startWeek, startDay, endWeek, endDay, self):
        self.clear(self.term.getDate(startWeek, startDay), self.term.getDate(endWeek, endDay))

    def clear(self):
        self.clear(0, 0, 19, 6)


class ScheduleTemplate(models.Model):

    name = models.CharField(max_length=20)

    eventgroup = models.ManyToManyField(EventGroup)

    # applies a schedule template to a schedule
    def apply(schedule, self):
        # iterate over event groups in this template
        for eventgrp in EventGroup.objects.filter(scheduletemplate=self.id):
            # iterate over each event inside each event group
            for event in Event.objects.filter(eventgroup=eventgrp.id):
                schedule.events.add(event)

    def apply(schedules, self):
        for schedule in schedules:
            self.apply(schedule)
