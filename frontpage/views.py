from django.shortcuts import get_object_or_404, render_to_response
from uppsala.shoutbox.models import shout
import hashlib


def index(request):
    if request.user.is_authenticated():
        logged_in = True
        user = request.user #Get the user
        shout_count = 5 #How many shouts will be shown?
        latest_shouts = fetch_latest_shouts(shout_count) #Get the shouts
        return render_to_response('frontpage/logged_in.html', {
                'logged_in' : logged_in,
                'user' : user,
                'latest_shouts' : latest_shouts,
                })

    else:
        logged_in = False
        return render_to_response('frontpage/not_logged_in.html', {
                'logged_in' : logged_in,
                })
  
 

def fetch_latest_shouts(count):
    latest_shouts = shout.objects.all().order_by('-pub_date')[:int(count)]
    gravatars = []
    for x in latest_shouts:
        x.gravatar = hashlib.md5(x.user.email).hexdigest()
    return latest_shouts
