from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from uppsala.shoutbox.models import shout
import hashlib

def index(request):
	latest_shouts_list = shout.objects.all().order_by('-pub_date')[:5]
	gravatars = []
	for x in latest_shouts_list:
		x.gravatar = hashlib.md5(x.user.email).hexdigest()
	return render_to_response('base_generic.html', {
		'latest_shouts': latest_shouts_list,
		})

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
				})
			else:
				yeniShout = shouts.create(shout = yazilmis, user = kullanici)
				return HttpResponseRedirect(reverse('uppsala.shoutbox.views.index'))
	else:
		kullanici = False
		return render_to_response('shoutbox/shout.html',{
				'error_message': "You need to login.",
			})
