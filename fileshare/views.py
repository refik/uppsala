from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse, HttpResponsePermanentRedirect
from django.template import RequestContext
from uppsala.settings import PROJECT_PATH,MEDIA_URL,ADMIN_MEDIA_PREFIX
from uppsala.fileshare.models import UploadedFile
from uppsala.fileshare.forms import *
from uppsala.radio import radio
from uppsala.decorators import *
import hashlib, os


@login_required
@rendered_with("fileshare/base_generic.html")
def index(request):
	shared_files = UploadedFile.objects.all()	
	form = UploadFileForm()
	media_url = MEDIA_URL
	for x in shared_files:
		x.gravatar = hashlib.md5(x.user.email).hexdigest()
	return locals()

def handle_uploaded_file(f,place):
	file_path = PROJECT_PATH + ADMIN_MEDIA_PREFIX + '%s/'%(place)  +str(f)
	destination = open(file_path, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	return file_path

@login_required
def addRadioFile(request,station):	
	kullanici = request.user
	shared_files = UploadedFile.objects.all()
	form = UploadFileForm(request.POST, request.FILES)
	if form.is_valid():
		name = request.FILES['file']
		place = 'radio_upload'
		path = handle_uploaded_file(name,place)
		newFile = shared_files.create(user = kullanici, file_path = path, file_name = str(name), is_public = True, share_to = kullanici)
		radio.add(station,path)
		radio.restart(station)
		return HttpResponseRedirect('/radio/'+str(station))	
#	return HttpResponsePermanentRedirect('/fileshare/')
#	return HttpResponse('Done, go back and refresh (this is a bug by the way)')

@login_required
def addFile(request):
	kullanici = request.user
	shared_files = UploadedFile.objects.all()
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			name = request.FILES['file']
			place = 'general_upload'
			path = handle_uploaded_file(name,place)
			newFile = shared_files.create(user = kullanici, file_path = path, file_name = str(name), is_public = True, share_to = kullanici)
			return HttpResponseRedirect('/')
		else:
			form = UploadFileForm()
	return render_to_response('fileshare/base_generic.html', {
			'form': form,
			}, context_instance=RequestContext(request))

		
