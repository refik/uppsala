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


def handle_uploaded_file(f,place):
	file_path = PROJECT_PATH + ADMIN_MEDIA_PREFIX + '%s/'%(place)
	checkUserFolder(file_path)
	file_path = PROJECT_PATH + ADMIN_MEDIA_PREFIX + '%s/'%(place)  +str(f)
	destination = open(file_path, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	return file_path


def addFile(request):
	kullanici = request.user
	shared_files = UploadedFile.objects.all()
	if request.method == 'POST':
		form = UploadFileForm(request.POST, request.FILES)
		if form.is_valid():
			name = request.FILES['file']
			fname = str(name)
			place = kullanici.username
			path = handle_uploaded_file(name,place)
			if fname[-3:] == "mp3" or fname[-3:] == "ogg":
				ftype = "Audio"
			if fname[-3:] == "jpg" or fname[-3:] == "gif" or fname[-3:] == "png":
				ftype = "Image"
			if fname[-3:] == "avi" or fname[-3:] == "mkv" or fname[-3:] == "ogv":
				ftype = "Audio"
			newFile = shared_files.create(user = kullanici, file_path = path, file_name = fname, file_type = ftype, is_public = True, share_to = kullanici)
			if request.POST['type'] == 'radio':
				station = request.POST['station']
				radio.add(station,path)
				radio.restart(station)
				return HttpResponseRedirect('/radio/'+str(station))
			return HttpResponseRedirect('/')
		else:
			form = UploadFileForm()
			return render_to_response('base.html', {
					'form': form,
					}, context_instance=RequestContext(request))

def checkUserFolder(path_name):
	if os.path.isdir(path_name) == False:
		os.mkdir(path_name)
		os.system('touch %s/folder'%(path_name))
