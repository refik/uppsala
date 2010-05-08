from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from uppsala.fileshare.forms import *
from uppsala.radio import radio

def index(request):
	stations = radio.stations()
	return render_to_response('radio/base.html', {'stations': stations})

def detail(request, station_id):
	form = UploadFileForm()
	return render_to_response('radio/station.html', {
		'songs': radio.songs(station_id), 
		'station_id': station_id,
		'form': form})

def new(request):
   new_s = request.POST['station']
   radio.new(new_s)
   return HttpResponseRedirect('/radio')

