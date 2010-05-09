from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from uppsala.fileshare.forms import *
from uppsala.radio import radio

@login_required
def index(request):
	stations = radio.stations()
	return render_to_response('radio/base.html', {'stations': stations,
						      })
@login_required
def detail(request, station_id):
	form = UploadFileForm()
	return render_to_response('radio/station.html', {
		'songs': radio.songs(station_id), 
		'station_id': station_id,
		'form': form,
		})

@login_required
def new(request):
   new_s = request.POST['station']
   radio.new(new_s)
   return HttpResponseRedirect('/')

