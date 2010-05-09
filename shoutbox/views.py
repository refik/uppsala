from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from uppsala.shoutbox.models import shout
import hashlib

@login_required
def index(request):
	latest_shouts_list = shout.objects.all().order_by('-pub_date')[:5]
	gravatars = []
	for x in latest_shouts_list:
		x.gravatar = hashlib.md5(x.user.email).hexdigest()
	return render_to_response('shoutbox/base_generic.html', {
			'latest_shouts': latest_shouts_list,
			},context_instance=RequestContext(request))

@login_required
def addShout(request):
	if request.user.is_authenticated():
		kullanici = request.user
		shouts = shout.objects.all()
		if len(request.POST['shout']) > 0:
			try:
				yazilmis = request.POST['shout']
			except (KeyError):
				return render_to_response('shoutbox/shout.html',{
						'error_message': "Please enter a shout",
						},context_instance=RequestContext(request))
			else:
				yeniShout = shouts.create(shout = yazilmis, user = kullanici)
				return HttpResponseRedirect('/')
	else:
		kullanici = False
		return render_to_response('shoutbox/shout.html',{
				'error_message': "You need to login.",
				},context_instance=RequestContext(request))
