from django.shortcuts import render_to_response, get_object_or_404
from uppsala.meet.models import Meet
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

def index(request):
    meeting_suggestions = Meet.objects.all()
    return render_to_response('meet/index.html', {'meeting_suggestions': meeting_suggestions})

def result(request, meet_id):
    p = get_object_or_404(Meet, pk=meet_id)
    return render_to_response('meet/result.html', {'meet': p})

def detail(request, meet_id):
    p = get_object_or_404(Meet, pk=meet_id)
    return render_to_response('meet/detail.html', {'meet': p})

def vote(request, meet_id):
    p = get_object_or_404(Meet, pk=meet_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the meet voting form.
        return render_to_response('meet/detail.html', {
            'meet': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.vote += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('uppsala.meet.views.result', args=(p.id,)))

def comment(request, meet_id):
    p = get_object_or_404(Meet, pk=meet_id)
    comment_new = request.POST['comment']
    sender_new = request.POST['sender']
    p.comment_set.create(comment=comment_new, sender=sender_new)
    p.save()
    return HttpResponseRedirect(reverse('uppsala.meet.views.result', args=(p.id,)))

def new(request):
    return render_to_response('meet/new.html')

def create(request):
    sender_new = request.POST['sender']
    date_new = request.POST['date']
    place_new = request.POST['place']
    n = Meet(date=date_new, place=place_new, sender=sender_new)
    n.save()
    n.choice_set.create(choice='gelirim', vote=0)
    n.choice_set.create(choice='gunde anlastik', vote=0)
    n.choice_set.create(choice='emin degilim', vote=0)
    n.choice_set.create(choice='gelemem', vote=0) 
    n.save()
    return HttpResponseRedirect(reverse('uppsala.meet.views.result', args=(n.id,)))


