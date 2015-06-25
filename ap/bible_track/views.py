from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
#from django.views.decorators.csrf import csrf_exempt

from bible_track.models import bible_book, tracker, Trainee
from terms.models import Term

#@csrf_exempt
def index(request):
	myUser = request.user;

	#AJAX for first-year and second-year bible reading 
	if request.is_ajax():
		try:
			#Setup
			isChecked = request.POST['checked']		
			myYear = request.POST['year']

			#If checked, adds book to the database
			if isChecked=="true":
				selected_book = tracker(trainee=myUser.trainee, book=bible_book.objects.get(id=request.POST['book']), year=myYear)
				selected_book.save()
			#If not checked, deletes book from the database
			else:
				selected_book = tracker.objects.filter(trainee=myUser.trainee)
				selected_book = selected_book.filter(book=request.POST['book'])
				selected_book = selected_book.filter(year=myYear)
				selected_book.delete()
			
			#Calculates how much the progress bar changes for both first-year and second-year bible reading	
			user_checked_list = tracker.objects.filter(trainee=myUser.trainee)
			if( myYear == "1" ):
				first_year_checked_list = user_checked_list.filter(year=1)
				first_year_progress = 0;
				for checked_book in first_year_checked_list:
					first_year_progress = first_year_progress + checked_book.book.verses
					
				first_year_progress = int(float(first_year_progress)/31103.0 * 100)
				return HttpResponse(str(first_year_progress))
			else:
				second_year_checked_list = user_checked_list.filter(year=2)
				second_year_progress = 0;
				for checked_book in second_year_checked_list:
					second_year_progress = second_year_progress + checked_book.book.verses;
				second_year_progress = int(float(second_year_progress)/7958.0 * 100);
				return HttpResponse(str(second_year_progress))
		except:
			selected_book = 0
	else:
		selected_book = 0

	#Default for Daily Bible Reading
	current_term = Term.current_term()


	#Default for First-year and Second-year bible reading
	bible_book_list = bible_book.objects.all()
	user_checked_list = tracker.objects.filter(trainee=myUser.trainee)
	first_year_checked_list = user_checked_list.filter(year=1)
	second_year_checked_list = user_checked_list.filter(year=2)
	
	first_year_progress = 0;
	for checked_book in first_year_checked_list:
		first_year_progress = first_year_progress + checked_book.book.verses
	first_year_progress = int(float(first_year_progress)/31103.0 * 100)

	second_year_progress = 0;
	for checked_book in second_year_checked_list:
		second_year_progress = second_year_progress + checked_book.book.verses
	second_year_progress = int(float(second_year_progress)/7958.0 * 100)
	
	first_year_is_complete = first_year_checked_list.count();
	year = int((myUser.trainee.current_term+1)/2);

	#Send data to the template!!!
	template = loader.get_template('bible_track/index.html')
	context = RequestContext(request, {
		'bible_book_list': bible_book_list,
		'first_year_checked_list': first_year_checked_list,
		'second_year_checked_list': second_year_checked_list,
		'first_year_is_complete': first_year_is_complete,
		'year': year,
		'first_year_progress': first_year_progress,
		'second_year_progress': second_year_progress,
	})
	return HttpResponse(template.render(context))

import datetime

def get_current_time(request):
  # Create a 'context' dictionary,
  # populate it with the current time
  # and return it
  context = {}
  context['current_time'] = datetime.datetime.now()
  return context
