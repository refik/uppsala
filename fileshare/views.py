from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from uppsala.fileshare.models import UploadedFile
from uppsala.fileshare.forms import *
from uppsala.settings import PROJECT_PATH,MEDIA_URL,ADMIN_MEDIA_PREFIX
import hashlib

def index(request):
	shared_files = UploadedFile.objects.all()
	form = UploadFileForm()
	for x in shared_files:
		x.gravatar = hashlib.md5(x.user.email).hexdigest()
	return render_to_response('fileshare/base_generic.html', {
		'shared_files': shared_files,
		'form': form,
		'media_url': MEDIA_URL,
		})

def handle_uploaded_file(f):
	file_path = PROJECT_PATH + ADMIN_MEDIA_PREFIX + str(f)
	destination = open(file_path, 'wb+')
	for chunk in f.chunks():
		destination.write(chunk)
	destination.close()
	return file_path

    
def addFile(request):
	if request.user.is_authenticated():
		kullanici = request.user
		shared_files = UploadedFile.objects.all()
		if request.method == 'POST':
			form = UploadFileForm(request.POST, request.FILES)
			
			if form.is_valid():
				name = request.FILES['file']
				path = handle_uploaded_file(name)
				print request.FILES['file']
				yeniFile = shared_files.create(user = kullanici, file_path = path, file_name = str(name), is_public = True, share_to = kullanici)
				return HttpResponseRedirect('/fileshare/')
			else:
				print "ahmet"
				form = UploadFileForm()
		return render_to_response('fileshare/base_generic.html', {
			'form': form,
			})
	else:
		kullanici = False
		return render_to_response('fileshare/base_generic.html',{
				'error_message': "You need to login.",
			})

		
