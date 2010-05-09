from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from uppsala.fileshare.forms import *
from uppsala.radio import radio
from uppsala.decorators import *


@login_required
@rendered_with("radio/base.html")
def index(request):
	stations = radio.stations()
	return locals()

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

