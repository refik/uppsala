from django.shortcuts import get_object_or_404, render_to_response
from django.contrib.auth.decorators import login_required
from uppsala.shoutbox.models import shout
from uppsala.meet.models import Meet
from uppsala.fileshare.models import UploadedFile
import hashlib
from uppsala.radio import radio
from uppsala.settings import MEDIA_URL


def index(request):
    if request.user.is_authenticated():
        logged_in = True
        user = request.user #Get the user

        shout_count = 5 #How many shouts will be shown?
        latest_shouts = fetch_latest_shouts(shout_count) #Get the shouts

        meetings_count = 5 #How many meetings will be shown?
        latest_meetings = fetch_meeting_suggestions(meetings_count)

        radio_stations = radio.stations()
        
        sharedFiles_count = 5 #How many files will be shown?
        latest_files = fetch_shared_files(sharedFiles_count)

        return render_to_response('frontpage/logged_in.html', {
                'logged_in' : logged_in,
                'user' : user,
                'latest_shouts' : latest_shouts,
                'meeting_suggestions' : latest_meetings,
                'stations' : radio_stations,
                'shared_files' : latest_files,
                'media_url' : MEDIA_URL,
                })

    else:
        logged_in = False
        return render_to_response('frontpage/not_logged_in.html', {
                'not_logged_in': True,
                'logged_in' : logged_in,
                })
  
 
def fetch_latest_shouts(count):
    latest_shouts = shout.objects.all().order_by('-pub_date')[:int(count)]
    gravatars = []
    for x in latest_shouts:
        x.gravatar = hashlib.md5(x.user.email).hexdigest()
    return latest_shouts

def fetch_meeting_suggestions(count):
    meeting_suggestions = Meet.objects.all().order_by('-date')[:int(count)]
    return meeting_suggestions

def fetch_shared_files(count):
    shared_files = UploadedFile.objects.all().order_by('-pub_date')[:int(count)]
    for x in shared_files:
        x.gravatar = hashlib.md5(x.user.email).hexdigest()
    return shared_files
