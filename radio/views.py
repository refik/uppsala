from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from uppsala.fileshare.forms import *
from uppsala.radio import radio
from uppsala.decorators import *


@login_required
@rendered_with("radio/station.html")
def detail(request, station_id):
	form = UploadFileForm()
	songs = radio.songs(station_id)
	return locals()

@login_required
def new(request):
   new_s = request.POST['station']
   radio.new(new_s)
   return HttpResponseRedirect('/')

@login_required
def restart(request,station_name):
	radio.restart(station_name)
	HttpResponseRedirect('/radio/'+str(station_name))

