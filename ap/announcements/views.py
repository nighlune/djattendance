from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView

from django.db import IntegrityError
from django.db import transaction


from .forms import NewAnnouncementForm
from django.contrib.messages.views import SuccessMessageMixin

from django.contrib import messages
from messages_extends import constants as constant_messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from accounts.models import Trainee
from .models import Announcement, TraineeMessage


class AnnouncementListView(ListView):
	model = Announcement
	template_name = 'announcements/announcement_list.html'

# class AnnouncementCreateView(SuccessMessageMixin, CreateView):
# 	model = Announcement
# 	form_class = NewAnnouncementForm
# 	success_url = reverse_lazy('announcements:announcement_list')
# 	success_message = "Announcement Has Been Made!"


class AnnouncementCreateView(TemplateView):
	template_name = 'announcements/announcement_create.html'
	form_class = NewAnnouncementForm

	def get_context_data(self, **kwargs):
		context = super(AnnouncementCreateView, self).get_context_data(**kwargs)
		return context

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			term = form.cleaned_data['term']
			gender = form.cleaned_data['gender']
			team = form.cleaned_data['team']
			hc = form.cleaned_data['hc']
			couple = form.cleaned_data['couple']
			message = form.cleaned_data['message']
			
			announcement = Announcement(term=term, gender=gender, team=team,
				hc=hc, couple=couple, message=message)
			try:
				announcement.save()
			except IntegrityError:
				transaction.rollback()


			# announcement to individual user
			if term != None :
				print(term)
				# sending the message to the user
			if gender != None:
				print(gender)
			if team != None :
				print(team)
			if hc != None :
				print(hc)
			if couple != None :
				print(couple)

			for trainee in Trainee.objects.all():
				traineeMessage = TraineeMessage.objects.create(read=False, trainee=trainee, announcement=announcement)
				traineeMessage.save()
			# announcement to multiple users
			# announcement to all users
			# elif send_to_all == True:
			# 	for user in User.objects.all():
			# 		messages.add_message(request, constant_messages.INFO_PERSISTENT, message, user=user, extra_tags="announcement")
			return HttpResponseRedirect(reverse_lazy('announcements:announcement_list'))
		return render(request, self.template_name, {'form': form})


