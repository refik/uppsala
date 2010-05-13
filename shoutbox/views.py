from django.contrib.auth.decorators import login_required
from uppsala.shoutbox.models import shout
from uppsala.decorators import *
import hashlib


@login_required
@rendered_with("base.html")
def addShout(request):
	kullanici = request.user
	shouts = shout.objects.all()
	if len(request.POST['shout']) > 0:
		try:
			yazilmis = request.POST['shout']
		except (KeyError):
			error_message = "Please enter a shout"
			return locals()
		else:
			shouts.create(shout = yazilmis, user = kullanici)			
			return locals()

