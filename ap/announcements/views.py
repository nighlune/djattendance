from django.views.generic.base import View, TemplateView
from .forms import NewAnnouncementForm
from django.contrib import messages
from messages_extends import constants as constant_messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse_lazy
from accounts.models import User


class AnnouncementListView(View):
	template_name = 'announcements/announcement_list.html'

class AnnouncementCreateView(TemplateView):
	template_name = 'announcements/announcement_create.html'
	form_class = NewAnnouncementForm

	def get_context_data(self, **kwargs):
		context = super(AnnouncementCreateView, self).get_context_data(**kwargs)
		context['number'] = 166
		return context

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})

	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			user = form.cleaned_data['user']
			send_to_all = form.cleaned_data['send_to_all']
			message = form.cleaned_data['message']
			
			# announcement to individual user
			if user != None and send_to_all == False:
				# sending the message to the user
				user = User.objects.get(pk=user.account_id)
				messages.add_message(request, constant_messages.INFO_PERSISTENT, message, user=user, extra_tags="announcement")
			# announcement to multiple users
			# announcement to all users
			elif send_to_all == True:
				for user in User.objects.all():
					messages.add_message(request, constant_messages.INFO_PERSISTENT, message, user=user, extra_tags="announcement")
			return HttpResponseRedirect(reverse_lazy('announcements:announcement_create'))
		return render(request, self.template_name, {'form': form})


