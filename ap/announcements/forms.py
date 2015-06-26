from django import forms
from .models import Announcement

class NewAnnouncementForm(forms.ModelForm):
	
	class Meta:
		model = Announcement

	def save(self, commit=True):
		announcement = super(NewAnnouncementForm, self).save(commit=False)
		if commit:
			announcement.save()
		return announcement

