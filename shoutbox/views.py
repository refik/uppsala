from django.shortcuts import render_to_response
from uppsala.shoutbox.models import shout

def index(request):
    latest_shouts_list = shout.objects.all().order_by('-pub_date')[:5]
    return render_to_response('shoutbox/index.html', {'latest_shouts': latest_shouts_list})
