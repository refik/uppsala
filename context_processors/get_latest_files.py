from django.conf import settings
from uppsala.settings import PROJECT_PATH,MEDIA_URL,ADMIN_MEDIA_PREFIX
from uppsala.fileshare.models import UploadedFile
from uppsala.fileshare.forms import *
import hashlib


def get_latest_files(request):
   "A context processor that provides the latest shared files" 
   shared_files = UploadedFile.objects.all()	
   form = UploadFileForm()
   media_url = MEDIA_URL
   for x in shared_files:
       x.gravatar = hashlib.md5(x.user.email).hexdigest()
   return locals()
