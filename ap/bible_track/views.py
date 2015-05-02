from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse
from django.template import RequestContext, loader
#from django.views.decorators.csrf import csrf_exempt

from bible_track.models import bible_book, tracker, Trainee
#from terms.models import Term

import random
'''def index(request):
    latest_question_list = bible_book.objects.order_by('name')[:5]
    #latest_question_list = bible_book.objects.all()
    output = ', '.join([p.name for p in latest_question_list])
    return HttpResponse(output)'''

#@csrf_exempt
def index(request):
	#if request.method == 'POST':
	print "HERE is Index"
	#myUser = request.user;
	myUser = request.user;
	if request.is_ajax():
		try:
			isChecked = request.POST['checked']
			#request.session['name1'] = "test"
			
			#print "Terms " + str(myUser.trainee_calculate_term)
			#print "Terms " + str(myUser.trainee.term.count())
			#print "Terms " + str(myUser.trainee.current_term)
			#myYear = int((myUser.trainee.current_term+1)/2);
			myYear = request.POST['year']
			print "Terms " + str(myYear)
            #
            #Term.objects.get(
			print str(isChecked)
			if isChecked=="true":
				#selected_book = tracker(trainee=Trainee.objects.get(id=1), book=bible_book.objects.get(id=request.POST['book']), year=myYear)
				selected_book = tracker(trainee=myUser.trainee, book=bible_book.objects.get(id=request.POST['book']), year=myYear)
				selected_book.save()
			else:
				#selected_book = tracker.objects.get(id=request.POST['book'])
				selected_book = tracker.objects.filter(book=request.POST['book'])
				#selected_book = selected_book.filter(trainee=Trainee.objects.get(id=1))
				selected_book = selected_book.filter(trainee=myUser.trainee)
				selected_book = selected_book.filter(year=myYear)
				selected_book.delete()
				print "deleted book"
				
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
			
				#DELETE ENTRY
			#selected_book = request.POST.get('choice')
			#selected_book = request.POST.get('book')
			#selected_book = tracker(trainee=Trainee.objects.get(id=1), book=bible_book.objects.get(id=2), year=1)
			#selected_book = tracker(trainee=Trainee.objects.get(id=1), book=bible_book.objects.get(id=request.POST.get('book')), year=2)
		except:
			selected_book = 0
		#return HttpResponse("You're looking at question " + str(selected_book))
	else:
		selected_book = random.randint(0, 10000);
	#p = get_object_or_404(bible_book)
	#selected_choice = p.choice_set.get(pk=request.POST['choice'])
	#request.POST.get('choice', False)
	#request.POST.get('choice')
	#selected_book = tracker(Trainee.objects.get(id=1), book=bible_book.objects.get(id=1), year=1)
	#selected_book.save()
	#latest_question_list = bible_book.objects.order_by('name')[:5]
	latest_question_list = bible_book.objects.all()
	#q = QueryDict('a=1&a=2&a=3', mutable=True)
	
	user_checked_list = tracker.objects.filter(trainee=myUser.trainee)
	first_year_checked_list = user_checked_list.filter(year=1)
	second_year_checked_list = user_checked_list.filter(year=2)
	
	first_year_progress = 0;
	for checked_book in first_year_checked_list:
		first_year_progress = first_year_progress + checked_book.book.verses;
	first_year_progress = int(float(first_year_progress)/31103.0 * 100);
	print "first_year_progress: " + str(first_year_progress)
	second_year_progress = 0;
	for checked_book in second_year_checked_list:
		second_year_progress = second_year_progress + checked_book.book.verses;
	second_year_progress = int(float(second_year_progress)/7958.0 * 100);	
	print "second_year_progress: " + str(second_year_progress)
	
	first_year_is_complete = first_year_checked_list.count();
	year = int((myUser.trainee.current_term+1)/2);
	template = loader.get_template('bible_track/index.html')
	context = RequestContext(request, {
		'latest_question_list': latest_question_list,
		'first_year_checked_list': first_year_checked_list,
		'second_year_checked_list': second_year_checked_list,
		'first_year_is_complete': first_year_is_complete,
		'year': year,
		'first_year_progress': first_year_progress,
		'second_year_progress': second_year_progress,
	})
	return HttpResponse(template.render(context))
    #return HttpResponse("You're looking at question %s." % question_id)

# Create your views here.
'''def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")'''
import datetime

def get_current_time(request):
  # Create a 'context' dictionary,
  # populate it with the current time
  # and return it
  context = {}
  context['current_time'] = datetime.datetime.now()
  return context


#def detail(request, question_id):
#    return HttpResponse("You're looking at question %s." % question_id)

#def results(request, question_id):
#    response = "You're looking at the results of question %s."
#    return HttpResponse(response % question_id)

#def vote(request, question_id):
#    return HttpResponse("You're voting on question %s." % question_id)
    
