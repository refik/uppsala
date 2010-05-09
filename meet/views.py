from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from uppsala.meet.models import Meet
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from uppsala.meet.forms import *
from uppsala.decorators import *

@login_required
@rendered_with("meet/index.html")
def index(request):
	meeting_suggestions = Meet.objects.all()
	return locals()

@login_required
@rendered_with("meet/result.html")
def result(request, meet_id):
	meet = get_object_or_404(Meet, pk=meet_id)
	return locals()

@login_required
@rendered_with("meet/detail.html")
def detail(request, meet_id):
	meet = get_object_or_404(Meet, pk=meet_id)
	return locals()

@login_required
@rendered_with("meet/detail.html")
def vote(request, meet_id):
	meet = get_object_or_404(Meet, pk=meet_id)
	try:
		selected_choice = p.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		error_message = "You didn't select a choice"
		return locals()		
	else:
		selected_choice.vote += 1
		selected_choice.save()
		return locals()

@rendered_with("meet/new.html")
def new(request):
	return locals()

@login_required
@rendered_with("meet/result.html")
def create(request):
	form = newMeet(request.POST)
	if form.is_valid()
		sender_new = request.user
		date_new = form.cleaned_data['date']
		place_new = form.cleaned_data['place']    
		meet = Meet(date=date_new, place=place_new, sender=sender_new)
		meet.save()
		meet.choice_set.create(choice='gelirim', vote=0)
		meet.choice_set.create(choice='gunde anlastik', vote=0)
		meet.choice_set.create(choice='emin degilim', vote=0)
		meet.choice_set.create(choice='gelemem', vote=0) 
		meet.save()
		return locals()
	
